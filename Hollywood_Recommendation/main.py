import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

st.set_page_config(page_title='Movie Recommemder',page_icon=":🎥:",layout='wide')
st.markdown("<h1 style='text-align: center; color: black;'>Hollywood Movie Recommender</h1>", unsafe_allow_html=True)
lottie_coding = load_lottiefile("38568-action.json")


c1, c2, c3 , c4, c5 = st.columns(5)

with c1:
    pass
with c2:
    pass
with c4:
    pass
with c5:
    pass
with c3 :
    st_lottie(
        lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",  # medium ; high
        # renderer="svg", # canvas
        height=110,
        width=110,
        key=None,
    )


yearslist1 = pickle.load(open('yearslist.pkl','rb'))
yearslist=pd.DataFrame(yearslist1)
with st.sidebar:
    selected=option_menu(menu_title=None,options=["Movies"],)
    if selected=="Movies":
        selected_option1 = st.selectbox(
            'From',
            sorted(yearslist['year'].unique()))
        selected2 = st.selectbox(
            'To',
            sorted(yearslist['year'].unique()))
    b = st.button('Get Movies')
    lst_movies=[]
    if b:
        for i in range(selected_option1,selected2,1):
            for k in range(len(yearslist['title'])):
                y=yearslist['year'][k]
                if( (y>=selected_option1) and (y <= selected2 )):
                    lst_movies.append(yearslist['title'][k])
    for i in lst_movies:
        st.write(i)


#if selected=="Movies":


def poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a81324a2c293f1104b097c2c85f86972&language=en=US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']



def recommed(movie):
        movieindex = list_of_movies[list_of_movies["title"] == movie].index[0]
        #print(movieindex)
        #print(list_of_movies.iloc[0].movie_id)
        distances = similarity[movieindex]
        rm = sorted(list(enumerate(similarity[movieindex])), reverse=True, key=lambda x: x[1])[1:11]
        movies_recommended=[]
        movie_posters=[]
        for i in rm:
            movie_id=list_of_movies.iloc[i[0]].movie_id
            print("movie _id",movie_id)
            movies_recommended.append(list_of_movies.iloc[i[0]].title)
            movie_posters.append(poster(movie_id))
        return movies_recommended,movie_posters


movies=pickle.load(open('hollywoodmovieslist.pkl','rb'))
list_of_movies= pd.DataFrame(movies)

similarity=pickle.load(open('hollywoodsimilarity.pkl','rb'))
#st.title("Hollywood Movie Recommendation System")




selected_option = st.selectbox(
    'Can you provide the name of a movie for which you would like me to provide suggestions??',
    list_of_movies['title'].values)

col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button('Recommend')


if center_button:
    result,p=recommed(selected_option)
    c1,c2,c3,c4,c5=st.columns(5)
    with c1:
        st.text(result[0])
        st.image(p[0])
    with c2:
        st.text(result[1])
        st.image(p[1])
    with c3:
        st.text(result[2])
        st.image(p[2])
    with c4:
        st.text(result[3])
        st.image(p[3])
    with c5:
        st.text(result[4])
        st.image(p[4])
    c6, c7, c8, c9=st.columns(4)
    with c6:
        st.text(result[5])
        st.image(p[5])
    with c7:
        st.text(result[6])
        st.image(p[6])
    with c8:
        st.text(result[7])
        st.image(p[7])
    with c9:
        st.text(result[8])
        st.image(p[8])
    #for i in result:
        #st.write(i)
popcorn = load_lottiefile("popcorn.json")
c1, c2, c3 , c4, c5 = st.columns(5)

with c1:
    pass
with c2:
    pass
with c4:
    pass
with c5:
    pass
with c3 :
    st_lottie(
        popcorn,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",  # medium ; high
        # renderer="svg", # canvas
        height=200,
        width=200,
        key=None,
    )












 #st.write("Link 1: <a href='http://localhost:8501/'>Example website</a>", unsafe_allow_html=True)
 #st.write("Link 2: <a href='http://www.google.com'>Google</a>", unsafe_allow_html=True)