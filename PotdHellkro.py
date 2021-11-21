#importar streamlit, requests y PIL
import streamlit as st
import requests
from PIL import Image

st.set_page_config(
    page_title="Picture of the Day",
    page_icon="rocket",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"})

url = 'https://api.nasa.gov/planetary/apod?api_key=' + st.secrets["MY_NASA_APIKEY"]

response = requests.get(url)
data = response.json()
st.title('Picture of the Day', anchor='center')

image = Image.open(requests.get(data['url'], stream=True).raw)
st.image(image, caption=data['title'], use_column_width=True)
st.write(data['explanation'])
st.write(data['copyright'])
st.write(data['date'])

