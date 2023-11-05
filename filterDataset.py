import pandas as pd




file_path = 'mobilerec_final.csv'
df = pd.read_csv(file_path, nrows=100000)



filtered_df = df[df['rating'] < 3].copy()  # Create a copy of the filtered DataFrame


output_csv_path = 'filtered_reviews.csv'

# Save the filtered dataset to a CSV file
filtered_df.to_csv(output_csv_path, index=False)  
# Define a function to preprocess text



