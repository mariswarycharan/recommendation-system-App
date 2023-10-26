import streamlit as st
import pandas as pd
from PIL import Image
import pickle
import requests 
from bs4 import BeautifulSoup 
import shutil
import os

st.set_page_config(page_title="home_page")

hide_st_style = """
            <style>
            # MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            # header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Customer Segmentation app")
read_data = pd.read_csv(r"purchase.csv")

def getdata(url):
    r = requests.get(url)
    return r.text

save_img_num = 1 
save_img_num_search = 1

def take_recommented_image(product_name):
    global save_img_num
    htmldata = getdata("https://www.google.com/search?q=" + "+".join(product_name.split(" "))  + "&sxsrf=AJOqlzWVCvnbecCF9YkHXrs2rN4d3cJUeQ:1676872151027&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiK2ZTHs6P9AhUT7jgGHfgtCngQ0pQJegQIBRAC&biw=1536&bih=714&dpr=1.25")
    soup = BeautifulSoup(htmldata, 'html.parser')

    imgdata = []
    for num,i in enumerate(soup.findAll('img',{"src":True})):
        if num == 5:
            break
        imgdata.append(i['src']) # made a change here so its appendig to the list

    
    filename = "E:/SRM_hackathon/images/images_set" + str(save_img_num) +"_" +"{}.jpg" 
    for i in range(len(imgdata)):
        print(f"img {i+1} / {len(imgdata)+1}")
    # try block because not everything in the imgdata list is a valid url
        try:
            r = requests.get(imgdata[i], stream=True)
            with open(filename.format(i), "wb") as f:
                f.write(r.content)
        except:
            print("Url is not an valid")

    save_img_num += 1

if 1==1:
    
    
    condition_allow = st.session_state["my_input"]
    
    initail_sub =  "Your Customer id is " + str(condition_allow)
    st.info(initail_sub)

    cus_buy_thing = []
    
    
    if str(condition_allow)[0:4] == "CUS_":
        
        if os.path.exists("images") == False:
            os.mkdir("images")
            os.mkdir("search_bar_images")
        
        st.subheader("Your purchase history:")
        # pur_button = st.button("Show Custumer purchase history")
        
        val = condition_allow
        
        predict_df = read_data[ read_data["Customer ID"] == val ]
        
        for i in predict_df.to_numpy():
            for j in i:
                j = str(j)
                if j != "nan" and j[0:4] != "CUS_":
                    cus_buy_thing.append(j)
    # if pur_button:           
    st.dataframe(pd.DataFrame(cus_buy_thing,columns=["purpose history"]))

    
    
    # if cus_buy_thing != []:
    initail_load_img_list = [ima for ima in os.listdir("images")]
    
    if len(initail_load_img_list) == 0:
    
        for product in cus_buy_thing:
            print("1111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
            take_recommented_image(product)
        
    st.subheader("Recommented for you!!!")

    for num,i in enumerate(cus_buy_thing):
        
        st.info(i)
        col1,col2,col3 = st.columns(3)
        with col1:
            st.image(Image.open(r"images\images_set"+ str(num+1) + "_1.jpg"))
        with col2:
            st.image(Image.open(r"images\images_set"+ str(num+1) + "_2.jpg"))
        with col3:
            st.image(Image.open(r"images\images_set"+ str(num+1) + "_3.jpg"))    
    

    # ---------------------------------------seach type --------------------------------------------------------------#
    
    st.subheader("look for the product")
      
    c1,c2 = st.columns(2)
    with c1:
        search_input = st.text_input("Enter the product name:")
    with c2:  
        st.markdown("")
        st.markdown("")
        seach_button = st.button("Search")
        
    

    if search_input != "":
        if seach_button:
            resultsinDataFrame = pickle.load(open(r"results.pickle","rb"))
            predict_product = resultsinDataFrame[resultsinDataFrame['Product 1'] == search_input].nlargest(n= 3 ,columns = 'Support')['Product 2']
            
            st.dataframe(pd.DataFrame(list(predict_product),columns=["Recommended"]))
            
            search_bar_find_img = list(predict_product)
            search_bar_find_img.insert(0,search_input)
            
            for product in search_bar_find_img:
                
                htmldata = getdata("https://www.google.com/search?q=" + "+".join(product.split(" "))  + "&sxsrf=AJOqlzWVCvnbecCF9YkHXrs2rN4d3cJUeQ:1676872151027&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiK2ZTHs6P9AhUT7jgGHfgtCngQ0pQJegQIBRAC&biw=1536&bih=714&dpr=1.25")
                soup = BeautifulSoup(htmldata, 'html.parser')

                imgdata = []
                for num,i in enumerate(soup.findAll('img',{"src":True})):
                    if num == 5:
                        break
                    imgdata.append(i['src']) # made a change here so its appendig to the list

                
                filename = "E:/SRM_hackathon/search_bar_images/images_set" + str(save_img_num_search) +"_" +"{}.jpg" 
                for i in range(len(imgdata)):
                    print(f"img {i+1} / {len(imgdata)+1}")
                # try block because not everything in the imgdata list is a valid url
                    try:
                        r = requests.get(imgdata[i], stream=True)
                        with open(filename.format(i), "wb") as f:
                            f.write(r.content)
                    except:
                        print("Url is not an valid")

                save_img_num_search += 1

            st.subheader("Do you want to buy these")

            for num,i in enumerate(search_bar_find_img):
                
                st.info(i)
                co1,co2,co3 = st.columns(3)
                with co1:
                    st.image(Image.open(r"search_bar_images\images_set"+ str(num+1) + "_1.jpg"))
                with co2:
                    st.image(Image.open(r"search_bar_images\images_set"+ str(num+1) + "_2.jpg"))
                with co3:
                    st.image(Image.open(r"search_bar_images\images_set"+ str(num+1) + "_3.jpg"))    
        
    

        
    
# # except:
# #     st.error("ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# #     pass  