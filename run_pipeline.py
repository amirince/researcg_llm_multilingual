import subprocess
import os

# Path to your virtual environment's Python interpreter
venv_python = os.path.join("framework_lib", "Scripts", "python.exe")  # For Windows
# venv_python = os.path.join('venv', 'bin', 'python')  # For macOS/Linux

# List of script names to run
scripts = [
    "1_zeroshot_framework.py",
    "2_fewshot_framework.py",
    "3_optimized_prompt.py",
    "4_optimized_prompts_framework.py",
]


def run_scripts_sequentially(script_list):
    for script in script_list:
        try:
            print(f"Running {script} using venv...")
            # Run the script using the venv Python interpreter and wait for it to finish
            result = subprocess.run([venv_python, script], check=True)
            print(f"{script} completed successfully!\n")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running {script}: {e}\n")
            break  # Stop the sequence if an error occurs


# Run the scripts sequentially
run_scripts_sequentially(scripts)
