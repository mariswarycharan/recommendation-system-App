import streamlit as st
import pandas as pd
import pickle
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from PIL import Image

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

if 1==1:
    condition_allow = st.session_state["my_input"]
    
    initail_sub =  "Customer id is " + str(condition_allow)
    st.info(initail_sub)
    
    
    if str(condition_allow)[0:4] == "CUS_":
        
        annual_income = st.number_input("Customer income in thousands :",1,200)
        customer_time_spend = st.number_input("Customer Spending Score (1-100) : ",1,100)
        no_of_cluster = st.number_input("Number of Clusters:",1,50)
        pred_button = st.button("Predict Cluster")
        X = pickle.load(open(r"input.pickle","rb"))
        kmeans = KMeans(n_clusters = no_of_cluster, init = 'k-means++', random_state = 42)
        y_kmeans = kmeans.fit_predict(X.iloc[:,[1,2]].values)
        X.insert(3,'cluster',y_kmeans,True)

        if pred_button:
            pred = kmeans.predict([[int(annual_income),int(customer_time_spend)]])
            st.success( "Customer belongs to Cluster " + str(pred[0]))
            
        
        colors = ['red','blue','green','indigo',"orange","purple","brown","gray","cyan","magenta",'pink','black',"beige"]
        
        for i in range(no_of_cluster):
            print(i)
            dat = X[X['cluster']==i]
            x = dat.iloc[:,1].values
            y = dat.iloc[:,2].values
            plt.scatter(x,y, s = 100, c =colors[i] , label = f'Cluster {i}')
            
        plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')

        plt.title('Clusters of customers')
        plt.xlabel('Annual Income (k$)')
        plt.ylabel('Spending Score (1-100)')
        plt.legend()
        # plt.show()
        plt.savefig("visualization_image_kmeans.png")
        
        st.image(Image.open("visualization_image_kmeans.png"))
        
    
        name_of_cluster = st.selectbox("Select the Cluster to show",[ "Cluster_" + str(i) for i in range(0,no_of_cluster) ])
        
        st.dataframe(X[X['cluster'] == int(name_of_cluster[-1]) ])
        
        
        
        
# except:
#     st.error("ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#     pass  