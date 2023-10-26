
import os
import shutil
import streamlit as st
import pandas as pd

# to initial setup for web app  
 
st.set_page_config(page_title="Login")

hide_st_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            # header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Login")
user_name = st.text_input("Your user id:")

login_button = st.button("Login")

read_data = pd.read_csv(r"purchase.csv")

if login_button == True:
    if user_name in list(read_data["Customer ID"]):
        st.success("You are login successfully!!!")
        if "my_input" not in st.session_state:
            st.session_state["my_input"] = ""
        # login_state = st.session_state["my_input"] 
        login_state = user_name
        
        st.session_state["my_input"] = login_state
    else:
        st.warning("Customer id does not exist")
        
        
    initail_load_img_list = [ima for ima in os.listdir("images")]
        
    if len(initail_load_img_list) != 0:
        
        shutil.rmtree("images")
        shutil.rmtree("search_bar_images")
    



# if login_button == True:
#     predicted = read_data[ (read_data["user_name"]  == str(user_name) ) & (read_data["password"] == str(password) )]
#     if user_name in list(predicted["user_name"]) and password in list(predicted["password"]):
#         st.success("You are login successfully!!!")
#         if "my_input" not in st.session_state:
#           st.session_state["my_input"] = ""
#         login_state = True
#         # login_state = st.session_state["my_input"] 
#         st.session_state["my_input"] = login_state
#     else:
#         st.warning("incorrect user name or password")
        
        
        
