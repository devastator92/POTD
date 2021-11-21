#importar streamlit, requests y PIL
import streamlit as st
import requests
from PIL import Image

st.set_page_config(
page_title="Picture of the Day",
page_icon="random",
layout="wide",
initial_sidebar_state="expanded",
menu_items={
'Get Help': 'https://www.extremelycoolapp.com/help',
'Report a bug': "https://www.extremelycoolapp.com/bug",
'About': "# This is a header. This is an *extremely* cool app!"})

url = 'https://api.nasa.gov/planetary/apod?api_key=WJsoSmfRyWRqydUZjIqIcuGeOasuLgzGTHHgOZAB'

response = requests.get(url)
data = response.json()
st.title('Astronomy Picture of the Day', anchor='center')
st.header('NASA Astronomy Picture of the Day')
st.subheader('Socio, usando Streamlit y python jojojojo')

image = Image.open(requests.get(data['url'], stream=True).raw)
st.image(image, caption=data['title'], use_column_width=True)
st.write(data['explanation'])
st.write(data['copyright'])
st.write(data['date'])