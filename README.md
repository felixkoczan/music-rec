#Music Recommender System
##Overview
This music recommendation system leverages the Spotify Million Song Dataset to recommend songs based on textual features (such as lyrics) combined with artist and genre metadata. The system uses Python for backend processing and Streamlit for a web-based interactive interface.

##Files Description
recommender.py: Core script that processes the dataset, computes TF-IDF vectors, and defines the recommendation logic.
app.py: Streamlit application for the web-based user interface.
df.pkl: Pickle file containing the preprocessed DataFrame.
tfidf_matrix.pkl: Pickle file containing the computed TF-IDF matrix.

##Dataset
The Spotify Million Song Dataset is a rich dataset that contains metadata and features for a million contemporary popular music tracks. For this project, the key attributes used are:

Song: The title of the song.
Artist: The name of the artist.
Genre: The genre of the song.
Text: Textual data, which could be lyrics or descriptive text about the song.

##Dependencies
pandas: Used for data manipulation and analysis.
numpy: Adds support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
sklearn: Machine learning library for Python. Used here for feature extraction (TF-IDF) and computing cosine similarity.
spotipy: A lightweight Python library for the Spotify Web API. Used for fetching song album covers.
streamlit: An open-source app framework for Machine Learning and Data Science projects.
pickle: Used for serializing and de-serializing Python object structures.

##Installation
Make sure to install all required packages using pip:

bash
Copy code
pip install pandas numpy sklearn spotipy streamlit


##Usage
###Data Preprocessing (recommender.py):

The dataset is loaded and preprocessed. Textual data are combined with artist and genre information to enrich the feature set.
The TfidfVectorizer from sklearn is used to transform the text data into a TF-IDF matrix.
Recommendation Function (recommender.py):

compute_similarity_for_song: Takes a song title, the TF-IDF matrix, and the DataFrame as input. Computes cosine similarity between the selected song's vector and all other vectors in the TF-IDF matrix. Returns a list of similar songs.

###Streamlit Web App (app.py):

The web app allows users to select a song from a dropdown. Upon selection, the app displays recommended songs along with their album covers (fetched using the Spotipy library).
Running the App:

Execute the Streamlit app with the command: streamlit run app.py.

###Functions and Classes
SpotifyClientCredentials (from Spotipy): Manages Spotify API authentication.
cosine_similarity (from sklearn): Computes the cosine similarity between vectors.
TfidfVectorizer (from sklearn): Converts a collection of raw documents to a matrix of TF-IDF features.
