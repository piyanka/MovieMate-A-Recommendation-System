import streamlit as st
import pickle
import pandas as pd
import requests
import joblib

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=2263e44adaef79b4d8934492766385dc&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/original" + poster_path
    return full_path

def recommend(movie):
    recommended_movies = []
    posters = []
    movie_index = new_df[new_df['title'] == movie].index[0]
    similar = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]

    for i in similar:
        movie_id = new_df.iloc[i[0]].movie_id
        recommended_movies.append(new_df.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return recommended_movies, posters

movies_list = pickle.load(open('movies.pkl','rb'))
movie = movies_list['title'].values
new_df = pd.DataFrame(movies_list)
similarity = joblib.load('similarity.joblib')


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'What is your Mood?',
    movie)
if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])


