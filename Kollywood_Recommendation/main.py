import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
import time

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

st.set_page_config(page_title='Movie Recommemder',page_icon=":🎥:",layout='wide')
st.markdown("<h1 style='text-align: center; color: black;'>Kollywood Movie Recommender</h1>", unsafe_allow_html=True)

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

yearslist1 = pickle.load(open('yearslistk.pkl','rb'))
yearslist=pd.DataFrame(yearslist1)
with st.sidebar:
    selected=option_menu(menu_title=None,options=["Movies"],key=time.time())
    if selected=="Movies":
        selected_option1 = st.selectbox(
            'From',
            sorted(yearslist['Release Year'].unique()))
        selected2 = st.selectbox(
            'To',
            sorted(yearslist['Release Year'].unique()))
    b = st.button('Get Movies')
    lst_movies=[]
    if b:
        for i in range(selected_option1,selected2 ,1):
            for k in range(len(yearslist['Title'])):
                y=yearslist['Release Year'][k]
                if( (y>=selected_option1) and (y <= selected2 )):
                    lst_movies.append(yearslist['Title'][k])
    for i in lst_movies:
        st.write(i)

def recommed(movie):
        movieindex = list_of_movies[list_of_movies["Title"] == movie].index[0]
        distances = similarity[movieindex]
        rm = sorted(list(enumerate(similarity[movieindex])), reverse=True, key=lambda x: x[1])[1:6]
        movies_recommended=[]
        for i in rm:
            idmovies=i[0]
            movies_recommended.append(list_of_movies.iloc[i[0]].Title)
        return movies_recommended

movies=pickle.load(open('movieslist.pkl','rb'))
list_of_movies= pd.DataFrame(movies)

similarity=pickle.load(open('similarity.pkl','rb'))

#st.title("Movie Recommender System")

selected_option = st.selectbox(
    'Can you provide the name of a movie for which you would like me to provide suggestions?',
    list_of_movies['Title'].values)

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
    result=recommed(selected_option)
    for i in result:
        st.write(i)

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

