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
st.title('Picture of the Day', anchor='center')

image = Image.open(requests.get(data['url'], stream=True).raw)
st.image(image, caption=data['title'], use_column_width=True)
st.write(data['explanation'])
st.write(data['copyright'])
st.write(data['date'])
