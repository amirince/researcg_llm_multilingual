import os

# Define the directory where your files are located
directory = 'codeswitched_results_re_run'

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the file ends with '_processed_processed.csv'
    if filename.endswith('_processed_processed.csv'):
        # Build the new filename by removing the extra '_processed'
        new_filename = filename.replace('_processed_processed.csv', '_processed.csv')
        
        # Get the full file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} -> {new_filename}')
