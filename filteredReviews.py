import pandas as pd

# Read the CSV file
file_path = 'filtered_reviews.csv'
df = pd.read_csv(file_path)

# Count the rows with "yes" value in the "security_issues" column
num_security_issues_yes_count = (df['security_issue'] == 'yes').sum()

security_issues_yes_df = df[df['security_issue'] == 'yes']

output_file_path = 'dataset.csv'
# Write the filtered DataFrame to the new CSV file without including the index
security_issues_yes_df.to_csv(output_file_path, index=False)

print(f"Number of rows with 'yes' in 'security_issues': {num_security_issues_yes_count}")
