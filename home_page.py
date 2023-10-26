import streamlit as st
import os

st.set_page_config(page_title="home_page",page_icon="Digital Docter\IMG_20211110_171634.jpg")

hide_st_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            # header {visibility: hidden;}
            </style>
            """
            
st.markdown(hide_st_style, unsafe_allow_html=True)

if os.path.exists("images") == False:
        os.mkdir("images")
        os.mkdir("search_bar_images")
            

