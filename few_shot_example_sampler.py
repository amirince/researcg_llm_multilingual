import pandas as pd

# Load the dataframe
dataframe = pd.read_csv(
    "codeswitched_results/llama31_8b/zero-shot/Telugu-English_test_processed.tsv",
    delimiter="\t",
)

# Filter the dataframe where the 'prediction' column is 'NIL'
filtered_df = dataframe[dataframe["prediction"] != "NIL"]

# Randomly sample 50 examples from the filtered dataframe
sampled_df = filtered_df.sample(
    n=50, random_state=42  # random_state for reproducibility
)

# Save the sampled examples to a CSV file
sampled_df.to_csv("sampled_examples.csv", index=False)

# Print the sampled examples
for index, row in sampled_df.iterrows():
    print(f"Example {index}: {row['sentence']}\nSentiment:\n")
