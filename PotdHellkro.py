#importar streamlit, requests y PIL
import streamlit as st
import requests
from PIL import Image

#add bootstrap css and js files to the page 
st.markdown("<style>body{background-color: #f0f8ff;}</style>", unsafe_allow_html=True)
st.markdown("<script src='https://code.jquery.com/jquery-3.3.1.slim.min.js' integrity='sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo' crossorigin='anonymous'></script>", unsafe_allow_html=True)
st.markdown("<script src='https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js' integrity='sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1' crossorigin='anonymous'></script>", unsafe_allow_html=True)
st.markdown("<script src='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js' integrity='sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM' crossorigin='anonymous'></script>", unsafe_allow_html=True)
st.markdown("<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'>", unsafe_allow_html=True)

#add navbar to the page 
st.markdown("<nav class='navbar navbar-expand-lg navbar-dark bg-dark'>", unsafe_allow_html=True)
st.markdown("<a class='navbar-brand' href='#'>PotdHellkro</a>", unsafe_allow_html=True)
st.markdown("<button class='navbar-toggler' type='button' data-toggle='collapse' data-target='#navbarSupportedContent' aria-controls='navbarSupportedContent' aria-expanded='false' aria-label='Toggle navigation'>", unsafe_allow_html=True)
st.markdown("<span class='navbar-toggler-icon'></span>", unsafe_allow_html=True)
st.markdown("</button>", unsafe_allow_html=True)
st.markdown("<div class='collapse navbar-collapse' id='navbarSupportedContent'>", unsafe_allow_html=True)
st.markdown("<ul class='navbar-nav mr-auto'>", unsafe_allow_html=True)
st.markdown("<li class='nav-item active'>", unsafe_allow_html=True)
st.markdown("<a class='nav-link' href='#'>Home <span class='sr-only'>(current)</span></a>", unsafe_allow_html=True)
st.markdown("</li>", unsafe_allow_html=True)
st.markdown("<li class='nav-item'>", unsafe_allow_html=True)
st.markdown("<a class='nav-link' href='#'>About</a>", unsafe_allow_html=True)
st.markdown("</li>", unsafe_allow_html=True)
st.markdown("<li class='nav-item'>", unsafe_allow_html=True)
st.markdown("<a class='nav-link' href='#'>Contact</a>", unsafe_allow_html=True)
st.markdown("</li>", unsafe_allow_html=True)
st.markdown("</ul>", unsafe_allow_html=True)

st.set_page_config(
page_title="Picture of the Day",
page_icon="random",
layout="centered",
initial_sidebar_state="expanded")

url = 'https://api.nasa.gov/planetary/apod?api_key=WJsoSmfRyWRqydUZjIqIcuGeOasuLgzGTHHgOZAB'

response = requests.get(url)
data = response.json()
st.title('Astronomy Picture of the Day', anchor='center')

image = Image.open(requests.get(data['url'], stream=True).raw)
st.image(image, caption=data['title'], use_column_width=True)
st.write(data['explanation'])
st.write(data['copyright'])
st.write(data['date'])