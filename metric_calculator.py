import pandas as pd
from sklearn.metrics import accuracy_score, precision_recall_fscore_support


def print_metrics(PATH):
    try:
        df = pd.read_csv(PATH, sep="\t")
    except:
        print("File Not Found!")
        return

    # Extract true labels and predictions
    y_true = df["sentiment"]
    y_pred = df["prediction"]

    # Calculate accuracy
    accuracy = accuracy_score(y_true, y_pred)

    # Calculate precision, recall, f1 score
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average="weighted", zero_division=1
    )

    # Print the results
    print(f"Accuracy: {accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall: {recall:.3f}")
    print(f"F1 Score: {f1:.3f}")


dataset_list = [
    "Hindi-English",
    "Malyalam-English",
    "Tamil-English",
    "Telugu-English",
]

tests = [
    "zero-shot",
    "few-shot",
    "optimized-prompt",
    "optimized_prompts_tuned_per_dataset",
]

for test in tests:
    print(test, "\n")
    for data_set in dataset_list:
        print(data_set)
        PATH = f"codeswitched_results\llama31_8b\{test}\{data_set}_test_processed.tsv"
        print_metrics(PATH)
        print("\n\n")
