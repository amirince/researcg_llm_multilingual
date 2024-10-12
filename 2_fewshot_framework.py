import pandas as pd
import asyncio
import os
import ollama
from ollama import AsyncClient
from fewshot_prompts import prompts
import time
import re

DATA_PATH = "data_sets/ary/test.tsv"

MODEL = "llama3.1:8b"


PROMPT = """You are a highly skilled classification assistant. Your task is to analyze the provided text and determine its sentiment. Classify the sentiment as one of the following: 'positive', 'negative', or 'neutral'. 

Please respond with just the sentiment label.

{sentiment}
"""


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
        self.model_name = re.sub(r'[<>:"/\\|?*]', "_", model)
        self.prompt = prompt
        self.label = label_col
        self.example_col = example_col
        self.dataset_name = dataset_name
        self.possible_sentiments = ["positive", "negative", "neutral"]
        self.data = pd.read_csv(data_path, delimiter="\t")
        self.data_path = data_path
        self.batch_size = batch_size
        self.all_labels = []

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
        # Parsing sentiment from LLM response:
        print(response)
        sentiment = response["message"]["content"]

        sentiment = sentiment.strip()
        sentiment = sentiment.lower()

        # Updated parsing logic
        if (
            "positive" in sentiment
            and "negative" not in sentiment
            and "neutral" not in sentiment
        ):
            return "positive"

        elif (
            "positive" not in sentiment
            and "negative" in sentiment
            and "neutral" not in sentiment
        ):
            return "negative"

        elif (
            "positive" not in sentiment
            and "negative" not in sentiment
            and "neutral" in sentiment
        ):
            return "neutral"

        else:  # On missclassification raise exception
            print(response)
            return "NIL"
            # raise ValueError("Example Misclassified!")

    def _save_results(self, current_batch_df):
        if not os.path.exists(f"codeswitched_results/{self.model_name}/few-shot"):
            os.makedirs(f"codeswitched_results/{self.model_name}/few-shot")

        file_name = os.path.basename(self.data_path)
        file_name_without_ext = os.path.splitext(file_name)[0]

        output_path = f"codeswitched_results/{self.model_name}/few-shot/{self.dataset_name}_{file_name_without_ext}_processed.tsv"

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
    # "Hindi-English",
    # "Malyalam-English",
    # "Tamil-English",
    # "Telugu-English",
    "Spanish-English"
]

for dataset in dataset_list:
    DATA_PATH = f"codeswitched_datasets/{dataset}/test.tsv"

    print(prompts[dataset])
    classifier = RunInference(
        data_path=DATA_PATH,
        dataset_name=dataset,
        batch_size=50,
        model="llama2:7b",
        prompt=prompts[dataset],
    )

    asyncio.run(classifier.run())
