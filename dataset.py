import pandas as pd
import random
import os

# Read the "mobilerec_final.csv" file
input_file_path = 'filtered_reviews.csv'
df = pd.read_csv(input_file_path)

# Randomly select 77 rows
random.seed(42)  # Set a seed for reproducibility
random_rows = random.sample(range(len(df)), 77)

# Create a DataFrame containing the randomly selected rows with "security_issue" set to "no"
selected_rows_df = df.iloc[random_rows].copy()
selected_rows_df['security_issue'] = 'no'

# Define the path for the "dataset.csv" file
output_file_path = 'dataset.csv'

# Check if the "dataset.csv" file already exists
if os.path.isfile(output_file_path):
    # Append the selected rows to the existing "dataset.csv" file
    selected_rows_df.to_csv(output_file_path, mode='a', header=False, index=False)
else:
    # If the file doesn't exist, create a new one with the selected rows
    selected_rows_df.to_csv(output_file_path, index=False)

print(f"Randomly selected 77 rows added to {output_file_path} with 'security_issue' set to 'no'.")
