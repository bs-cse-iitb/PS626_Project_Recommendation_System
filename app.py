import pickle
import streamlit as st
import pandas as pd


def recommend(movie):
    index = movies[movies['Title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_movies= []
    for i in distances[1:10]:
        movies_featurs=[]
        movies_featurs.append(movies.iloc[i[0]].Title)
        
        movies_featurs.append(round(movies.iloc[i[0]].IMDb,1))
        movies_featurs.append(movies.iloc[i[0]].Year)
        movies_featurs.append(movies.iloc[i[0]].Age)
        print(movies_featurs)
        recommend_movies.append(movies_featurs)

    return recommend_movies


st.header('Movies Recommendation System')
movies = pickle.load(open('Model/movies.pkl','rb'))
similarity = pickle.load(open('Model/similarity.pkl','rb'))

movies_list = movies['Title'].values
selected_movie = st.selectbox(
    "Select Movie Name",
    movies_list
)

if st.button('Recommend Movies'):
    recommended_movies = recommend(selected_movie)
    df = pd.DataFrame(recommended_movies, columns = ['Name', 'IMDb Rating','Year','Age'])
    st.table(df)