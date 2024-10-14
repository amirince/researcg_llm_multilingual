import pandas as pd
from sklearn.metrics import accuracy_score, precision_recall_fscore_support


def print_metrics(PATH):
    try:
        df = pd.read_csv(PATH, sep="\t")
    except FileNotFoundError:
        print("File Not Found!")
        return

    # Calculate the percentage of NIL examples
    total_samples = len(df)
    # print(f"Total Samples: {total_samples}")
    nil_samples = len(df[df["prediction"] == "NIL"])
    nil_percentage = (nil_samples / total_samples) * 100
    # print(f"Percentage of 'NIL' examples: {nil_percentage:.2f}%")

    # Filter out NIL examples
    df_filtered = df[df["prediction"] != "NIL"]

    # Record the sample size of the non-NIL data
    non_nil_sample_size = len(df_filtered)
    # print(f"Sample size after filtering 'NIL': {non_nil_sample_size}")

    # Ensure there are valid samples left after filtering
    if non_nil_sample_size == 0:
        print("No valid samples left after filtering.")
        return

    # Extract true labels and predictions
    y_true = df_filtered["sentiment"]
    y_pred = df_filtered["prediction"]

    # Calculate accuracy
    accuracy = accuracy_score(y_true, y_pred)
    # precision = precision_score(y_true, y_pred, average="weighted")
    # recall = recall_score(y_true, y_pred, average="weighted")
    # f1 = f1_score(y_true, y_pred, average="weighted")
    # Calculate precision, recall, f1 score
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average="weighted", zero_division=1
    )

    # Print the results
    print(f"{nil_percentage:.3f}%")
    print(f"{accuracy:.3f}")
    print(f"{precision:.3f}")
    print(f"{recall:.3f}")
    print(f"{f1:.3f}")
    print(f"{non_nil_sample_size}")


# def print_metrics(PATH):
#     try:
#         df = pd.read_csv(PATH, sep="\t")
#     except:
#         print("File Not Found!")
#         return

#     # Extract true labels and predictions
#     y_true = df["sentiment"]
#     y_pred = df["prediction"]

#     # Calculate accuracy
#     accuracy = accuracy_score(y_true, y_pred)

#     # Calculate precision, recall, f1 score
#     precision, recall, f1, _ = precision_recall_fscore_support(
#         y_true, y_pred, average="weighted", zero_division=1
#     )

#     # Print the results
#     print(f"Accuracy: {accuracy:.3f}")
#     print(f"Precision: {precision:.3f}")
#     print(f"Recall: {recall:.3f}")
#     print(f"F1 Score: {f1:.3f}")


dataset_list = [
    "Hindi-English",
    "Malyalam-English",
    "Tamil-English",
    "Telugu-English",
]

tests = [
    "zero-shot",
    "few-shot",
    "optimized_prompt",
    "optimized_prompts_tuned_per_dataset",
]


# models = ["llama2_7b", "llama3.1_8b", "llama3.2_1b", "llama3.2_3b"]
models = ["llama3.2_1b"]
for dataset in dataset_list:
    print(f"Dataset: {dataset}")
    for model in models:
        print(f"Model:{model}")
        for test in tests:
            print(f"Test: {test}")
            PATH = f"codeswitched_results_re_run/{model}/{test}/{dataset}_test_processed.tsv"
            print_metrics(PATH)
            print("\n\n")
