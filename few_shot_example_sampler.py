import pandas as pd

# Load the dataframe
dataframe = pd.read_csv(
    "codeswitched_results/llama31_8b/zero-shot/Telugu-English_test_processed.tsv",
    delimiter="\t",
)

# Filter the dataframe where the 'prediction' column is 'NIL'
filtered_df = dataframe[dataframe["prediction"] == "NIL"]

# Randomly sample 5 examples from the filtered dataframe
sampled_df = filtered_df.sample(
    n=5, random_state=42
)  # random_state for reproducibility


for index, row in sampled_df.iterrows():
    print(f"Example {index}: {row['sentence']}\nSentiment: {row['sentiment']}\n")
