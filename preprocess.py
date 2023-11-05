import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Read the combined dataset
dataset_path = 'combined_dataset.csv'
df = pd.read_csv(dataset_path)

# Text preprocessing function
def preprocess_text(text):
    # Remove special characters, symbols, and HTML tags
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenization
    tokens = word_tokenize(text)

    # Lowercasing and stopwords removal
    stop_words = set(stopwords.words('english'))
    tokens = [word.lower() for word in tokens if word.lower() not in stop_words]

    # Join tokens back into a cleaned text
    cleaned_text = ' '.join(tokens)
    
    return cleaned_text

# Apply text preprocessing to the "review" column
df['cleaned_review'] = df['review'].apply(preprocess_text)
df = df[df['cleaned_review'].str.strip() != '']

# Overwrite the existing CSV file with the cleaned data
df.to_csv(dataset_path, index=False)

# Example: TF-IDF vectorization
tfidf_vectorizer = TfidfVectorizer(max_features=1000)
X = tfidf_vectorizer.fit_transform(df['cleaned_review'])


