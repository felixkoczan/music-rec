# TuneTornado
## A music recommendation system
## Video Demo: https://www.youtube.com/watch?v=cDopfhQWA8U

## Description
Tune Tornado leverages the Spotify Million Song Dataset to recommend songs based on textual features (such as lyrics) combined with artist and genre metadata. The system uses Python for backend processing and Streamlit for a web-based interactive interface.

## Files Description

### recommender.py 
Core script that processes the dataset, computes TF-IDF vectors, and defines the recommendation logic.
### app.py 
Streamlit application for the web-based user interface.
### df.pkl
Pickle file containing the preprocessed DataFrame.
### tfidf_matrix.pkl 
Pickle file containing the computed TF-IDF matrix.

## Dataset

The Spotify Million Song Dataset is a rich dataset that contains metadata and features for a million contemporary popular music tracks. For this project, the key attributes used are:

Song: The title of the song.
Artist: The name of the artist.
Genre: The genre of the song.
Text: Textual data, which could be lyrics or descriptive text about the song.

## Dependencies

pandas: Used for data manipulation and analysis.
numpy: Adds support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
sklearn: Machine learning library for Python. Used here for feature extraction (TF-IDF) and computing cosine similarity.
spotipy: A lightweight Python library for the Spotify Web API. Used for fetching song album covers.
streamlit: An open-source app framework for Machine Learning and Data Science projects.
pickle: Used for serializing and de-serializing Python object structures.

## Installation

Make sure to install all required packages using pip:

bash
Copy code
pip install pandas numpy sklearn spotipy streamlit


## Usage

### Data Preprocessing (recommender.py):

The dataset is loaded and preprocessed. Textual data are combined with artist and genre information to enrich the feature set.
Feature Extraction with TF-IDF Vectorizer:

TfidfVectorizer from scikit-learn is employed to transform the preprocessed textual data into a TF-IDF matrix.

Term Frequency-Inverse Document Frequency (TF-IDF) is a statistical measure used to evaluate the importance of a word to a document in a collection or corpus. It increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus, which helps control for the fact that some words are generally more common.
Each row in the TF-IDF matrix represents a song, and each column represents a unique term. The values in the matrix reflect the importance of each term to the corresponding song.
Result:
The output of this preprocessing step is a structured DataFrame where each song is associated with its combined text, artist, along with a TF-IDF matrix representing the transformed textual data.
This structured and enriched data is then utilized in the recommendation logic to compute similarities between songs and generate song recommendations.

#### Recommendation Function (recommender.py):

Purpose:
This function is designed to compute and return a list of songs that are similar to a given song. The similarity is determined based on the features extracted from the songs' textual data (and possibly other attributes like artist and genre), transformed into a TF-IDF (Term Frequency-Inverse Document Frequency) matrix.

Parameters:
song: The title of the song for which recommendations are sought. It is a string representing the name of the song.
tfidf_matrix: A sparse matrix representing the TF-IDF features of all songs in the dataset. Each row corresponds to a song, and each column represents a unique feature (term) extracted from the textual data.
df: A pandas DataFrame that contains the metadata and features of the songs. It should have at least a column for the song titles.
Functionality:
The function first locates the index of the given song in the DataFrame (df).
Using this index, it retrieves the corresponding TF-IDF vector (row) from the tfidf_matrix.
Cosine similarity is then computed between this vector and all vectors in the TF-IDF matrix. This step essentially measures how similar the given song is to every other song in the dataset based on their TF-IDF features.
The similarities are sorted, and the indices of the top similar songs are retrieved.
Using these indices, the function then extracts the titles of the most similar songs from the DataFrame.
The function returns a list of these song titles, which are the recommendations.
Returns:
A list of song titles that are most similar to the input song. The number of recommended songs can be adjusted as needed (for example, the top 10 similar songs).

### Streamlit Web App (app.py):

The web app allows users to select a song from a dropdown. Upon selection, the app displays recommended songs along with their album covers (fetched using the Spotipy library).
Running the App:

Execute the Streamlit app with the command: streamlit run app.py.

### Functions and Classes

#### SpotifyClientCredentials (from Spotipy)
Purpose:
SpotifyClientCredentials is a class provided by the spotipy library, a lightweight Python library for the Spotify Web API. This class is specifically used for handling OAuth 2.0 authentication with Spotify, which is required to access most of Spotify's web API endpoints.

Functionality:
Manages the process of authenticating with Spotify's API using the Client Credentials Flow.
Requires a Spotify Developer account where you register your application to obtain a client_id and client_secret.
Generates an access token that is used in subsequent API requests to Spotify. This token is valid for a limited period and is automatically refreshed by the class as needed.

#### cosine_similarity (from sklearn)
Purpose:
cosine_similarity is a function in the scikit-learn library that computes the cosine similarity between vectors. It is commonly used in information retrieval and text mining to measure the similarity between documents.

Functionality:
Takes two sets of vectors and computes the cosine similarity between each pair of vectors.
The cosine similarity is a measure that calculates the cosine of the angle between two vectors in a multi-dimensional space.
The result ranges from -1 (meaning exactly opposite) to 1 (exactly the same), with 0 typically indicating independence.TfidfVectorizer (from sklearn): Converts a collection of raw documents to a matrix of TF-IDF features.

#### TfidfVectorizer (from sklearn)
Purpose:
TfidfVectorizer is a class in the scikit-learn library that converts a collection of raw documents to a matrix of TF-IDF (Term Frequency-Inverse Document Frequency) features. It is widely used in text mining and natural language processing.

Functionality:
Analyzes and preprocesses text data: tokenization, counting, normalization, and weighting with TF-IDF.
Term Frequency (TF): Measures how frequently a term occurs in a document.
Inverse Document Frequency (IDF): Measures how important a term is within the entire corpus.
The resulting TF-IDF features are often used in algorithms for text analysis, such as clustering or text classification.
