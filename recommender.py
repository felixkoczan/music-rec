import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load Dataset
df = pd.read_csv('C:/Users/felix/music-rec/data/spotify_millsongdata.csv')

# Preprocess and combine text, artist, and genre into a single feature
df['combined_features'] = df['text'].str.lower() + ' ' + df['artist'].str.lower()
df['combined_features'] = df['combined_features'].replace(r'\s+', ' ', regex=True)

# Using TfidfVectorizer with combined features
tfidf_vectorizer = TfidfVectorizer(analyzer='word', stop_words='english', max_features=10000)
tfidf_matrix = tfidf_vectorizer.fit_transform(df['combined_features'])

# Function to compute similarity for a specific song
def compute_similarity_for_song(song, tfidf_matrix, df):
    song_idx = df[df['song'] == song].index[0]
    song_feature = tfidf_matrix[song_idx]
    similarity = cosine_similarity(song_feature, tfidf_matrix).flatten()
    similar_indices = similarity.argsort()[-11:-1][::-1]
    return df.iloc[similar_indices]['song'].tolist()

# Example usage
recommended_songs = compute_similarity_for_song('Fernando', tfidf_matrix, df)
print(recommended_songs)

# Pickle the TF-IDF matrix and the DataFrame
pickle.dump(tfidf_matrix, open('tfidf_matrix.pkl', 'wb'))
pickle.dump(df, open('df.pkl', 'wb'))
