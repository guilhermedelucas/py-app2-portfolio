import streamlit as st
import pandas
from send_email import send_email

df = pandas.read_csv('pages/topics.csv')

select_options = [row['topic'] for i, row in df.iterrows()]

with st.form(key='contact_us'):
    email = st.text_input(label="Your email address", key="email")
    topic = st.selectbox(label="What topic do you want to discuss?", key="topic", options=select_options)
    message = st.text_area(label="Your message", key="message")
    button = st.form_submit_button('Send')

    if button:
        send_email(email=email, topic=topic, message=message)
        st.info('Your email was sent')