import os
import shutil


def copy_files_with_structure(main_directory, new_directory):
    # Walk through the main directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(main_directory):
        for filename in filenames:
            # Check if the file is named 'Spanish-English_test_processed.tsv'
            if filename == "Spanish-English_test_processed.tsv":
                # Create the relative path from the main_directory
                relative_path = os.path.relpath(dirpath, main_directory)

                # Create the corresponding directory in the new directory
                new_dir_path = os.path.join(new_directory, relative_path)
                os.makedirs(new_dir_path, exist_ok=True)  # Ensure the folder exists

                # Define full paths for copying
                source_file = os.path.join(dirpath, filename)
                destination_file = os.path.join(new_dir_path, filename)

                # Copy the file to the new directory
                shutil.copy2(source_file, destination_file)  # copy2 preserves metadata
                print(f"Copied: {source_file} to {destination_file}")


# Example usage
main_directory = "codeswitched_results_re_run"
new_directory = "results"
copy_files_with_structure(main_directory, new_directory)
