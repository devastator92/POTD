import streamlit as st
import requests
from PIL import Image

st.set_page_config(
page_title="Picture of the Day",
page_icon="rocket",
layout="centered",
initial_sidebar_state="expanded",
)

url = 'https://api.nasa.gov/planetary/apod?api_key=' + st.secrets["MY_NASA_APIKEY"]

response = requests.get(url)
data = response.json()
st.markdown("<h1 style='text-align: center; color: black;'>NASA Picture of the Day</h1>", unsafe_allow_html=True)

image = Image.open(requests.get(data['url'], stream=True).raw)
st.image(image, caption=data['title'], use_column_width=True)
explanation = data['explanation']
st.markdown("<p style='text-align: justify; color: black;'>" + explanation + "</p>", unsafe_allow_html=True)
st.write(data['copyright'])
st.write(data['date'])
