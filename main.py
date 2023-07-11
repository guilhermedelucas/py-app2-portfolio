import streamlit as st

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
    st.write(content)


content2 = """Bellow you can find some of the apps I have built in Python. Feel free to contact me!"""
st.write(content2)