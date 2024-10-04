import pandas as pd
import asyncio
import os
from ollama import AsyncClient
import time

DATA_PATH = "data_sets/ary/test.tsv"

MODEL = "llama3.1:8b"

PROMPT = """Analyze the sentiment of the text and categorize it as 'Positive', 'Neutral', or 'Negative'. 
A text is 'Positive' when it conveys clear or subtle expressions of happiness, satisfaction, or approval, 
like 'The event was a joy to attend' or 'I appreciate your hard work on this'. 
Texts are 'Neutral' when they provide information or facts without a strong emotional tone, even if they include minor positive or 
negative connotations, such as 'This phone model has a larger screen'. 
Texts that contain both positive and negative elements should be classified based on the most prevalent sentiment. 
If the negative elements are not overpowering, consider the text 'Positive'. Assign the 'Negative' label only when negative feelings like 
dissatisfaction or disappointment are the primary focus of the text, as in 'I'm frustrated with the constant delays'. 
Be particularly cautious in assessing subtle positive cues and ensure that neutral texts with minor emotive language are not misclassified 
as 'Positive' or 'Negative'."""


EXAMPLE_COL = "sentence"
LABEL_COL = "sentiment"


class RunInference:

    def __init__(
        self,
        data_path,
        dataset_name,
        batch_size=50,
        model="llama3.1:8b",
        prompt=PROMPT,
        example_col=EXAMPLE_COL,
        label_col=LABEL_COL,
    ) -> None:
        self.model = model
        self.prompt = prompt
        self.label = label_col
        self.example_col = example_col
        self.dataset_name = dataset_name
        self.possible_sentiments = ["positive", "negative", "neutral"]
        self.data = pd.read_csv(data_path, delimiter="\t")
        self.data_path = data_path
        self.batch_size = batch_size
        self.all_labels = []

        self.data = self.data.head(1)

    async def classify_text(self, example):
        response = await AsyncClient().chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": self.prompt,
                },
                {
                    "role": "user",
                    "content": example,
                },
            ],
        )
        sentiment = response["message"]["content"]

        sentiment = sentiment.strip()
        sentiment = sentiment.lower()

        if sentiment not in self.possible_sentiments:
            raise ValueError("Example Misclassified!")

        return sentiment

    def _save_results(self, current_batch_df):
        if not os.path.exists("codeswitched_results/llama31_8b/optimized-prompt"):
            os.makedirs("codeswitched_results/llama31_8b/optimized-prompt")

        file_name = os.path.basename(self.data_path)
        file_name_without_ext = os.path.splitext(file_name)[0]

        output_path = f"codeswitched_results/llama31_8b/optimized-prompt/{self.dataset_name}_{file_name_without_ext}_processed.tsv"

        results_df = pd.DataFrame(self.all_labels, columns=["prediction"])
        current_batch_df["prediction"] = results_df["prediction"][
            -len(current_batch_df) :
        ]
        current_batch_df.to_csv(
            output_path,
            sep="\t",
            index=False,
            mode="a",
            header=not os.path.exists(output_path),
        )

        print(f"Batch results saved to {output_path}")

    async def process_batch(self, batch_df):
        max_retries = 1
        labels = []

        for idx, row in batch_df.iterrows():
            retries = 0
            success = False
            label = None

            while not success and retries < max_retries:
                try:
                    print("Example: ", idx)
                    label = await self.classify_text(row[self.example_col])
                    success = True
                except Exception as e:
                    retries += 1
                    print(f"Error classifying example {idx}")

            if success:
                labels.append(label)
            else:
                labels.append("NIL")
                print(f"Failed to classify example {idx} after {max_retries} attempts.")

        self.all_labels.extend(labels)
        self._save_results(batch_df)

    async def run(self):

        start_time = time.time()

        total_rows = len(self.data)
        for start in range(0, total_rows, self.batch_size):
            end = min(start + self.batch_size, total_rows)
            batch_df = self.data.iloc[start:end]
            await self.process_batch(batch_df)

        end_time = time.time()
        duration = end_time - start_time
        print(f"Processing completed in {duration:.2f} seconds.")


dataset_list = [
    "Hindi-English",
    "Malyalam-English",
    "Spanish-English",
    "Tamil-English",
    "Telugu-English",
]

for dataset in dataset_list:
    DATA_PATH = f"codeswitched_datasets/{dataset}/test.tsv"
    classifier = RunInference(
        data_path=DATA_PATH, dataset_name=dataset, batch_size=50, model="llama3.1:8b"
    )

    asyncio.run(classifier.run())
    time.sleep(
        0
    )  # sleep let GPU throttle down and cool off before working on next dataset
