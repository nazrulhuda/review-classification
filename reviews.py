import pandas as pd

file_path = 'mobilerec_final.csv'
df = pd.read_csv(file_path, nrows=100000)



filtered_df = df[df['rating'] < 3].copy()  # Create a copy of the filtered DataFrame

num_rows = filtered_df.shape[0]
print(f"Number of rows in the DataFrame: {num_rows}")


print(filtered_df.columns)
print(filtered_df.head())
