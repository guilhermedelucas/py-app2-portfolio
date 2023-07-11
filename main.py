import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")


with col2:
    st.title('Guilherme de Lucas')
    content = """Hi, I am Guilherme! I am a javascript developer, learning Python. 
    My development career starts in 2016, when I studied at Spiced Academy, and on 
    2017 started my first developer job at Dots. Now I am looking to expand my 
    career and learn about Machine Learning and AI"""
    st.info(content)


content2 = """Bellow you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content2)

col3, emptycol, col4 = st.columns([1.5, 0.5, 1.5])


df = pandas.read_csv('data.csv', sep=";")


def display_app(row_local):
    st.header(row_local['title'])
    st.write(row_local['description'])
    st.image(f"images/{row_local['image']}")
    st.write(f"[Source_code]({row_local['url']})")


with col3:
    for index, row in df[:10].iterrows():
        display_app(row)


with col4:
    for index, row in df[10:].iterrows():
        display_app(row)


# with col4: