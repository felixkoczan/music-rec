import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from sklearn.metrics.pairwise import cosine_similarity

# Spotify client credentials (replace with your credentials)
CLIENT_ID = "b939c064215a48a78f21d815089ae564"
CLIENT_SECRET = "3637caf08ffd438cbbf6eebf39c747ca"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend(song, df, tfidf_matrix):
    # Find the index of the song in the dataframe
    song_idx = df[df['song'] == song].index[0]

    # Compute cosine similarity between this song's features and all songs' features
    song_feature = tfidf_matrix[song_idx]
    similarity = cosine_similarity(song_feature, tfidf_matrix).flatten()

    # Get top recommendations
    recommended_indexes = similarity.argsort()[-6:-1][::-1]
    recommended_songs = df.iloc[recommended_indexes]
    
    recommended_music_names = recommended_songs['song'].tolist()
    recommended_music_posters = [get_song_album_cover_url(song, artist) for song, artist in zip(recommended_songs['song'], recommended_songs['artist'])]

    return recommended_music_names, recommended_music_posters

st.set_page_config(page_title="Music Recommender", page_icon="🎵", layout="wide")
st.title('🎶 Music Recommender System')

df = pickle.load(open('df.pkl', 'rb'))
tfidf_matrix = pickle.load(open('tfidf_matrix.pkl', 'rb'))

with st.sidebar:
    st.header("Select a Song")
    selected_song = st.selectbox("Type or select from the dropdown", df['song'].values)

st.header("Recommended Songs")
if st.button('Show Recommendation'):
    recommended_music_names, recommended_music_posters = recommend(selected_song, df, tfidf_matrix)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]

    for i, col in enumerate(columns):
        with col:
            if i < len(recommended_music_names):
                st.image(recommended_music_posters[i], width=150)
                st.caption(recommended_music_names[i])
