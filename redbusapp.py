import pandas as pd
import streamlit as st
import pymysql
from streamlit_option_menu import option_menu

# Database connection
conn = pymysql.connect(
    host="localhost",      
    user="root",  
    password="1234",    
    database="red_bus_details"
        )
cursor = conn.cursor()

st.set_page_config(page_title= "RedbusApp", layout= "wide")
with st.sidebar:
    
    st.sidebar.image(r"C:\Users\devap\OneDrive\Desktop\Scraping file\red bus project\OIP.jpg", use_container_width=True)

    page = option_menu(
    
                menu_title = "Select Any Menu",
                options = ["Home", "States & Routes"],
                styles = {
                    "nav-link-selected": {"background-color": "Red"}
                }
    )
    
# Home page settings
if page == "Home":
    st.title("*Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit*")
    st.subheader("*Domain : Transportation*")
    st.subheader("*Objective*")
    st.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data")
    st.header("*Skills Required for This Project*")
    st.subheader("*Python Programming*")
    st.markdown("Proficiency in Python for data manipulation, web scraping, and automating tasks using libraries like Selenium, Pandas, and Streamlit.")
    st.subheader("*Web Scraping*")
    st.markdown(" Experience with Selenium for extracting dynamic web content from websites that use JavaScript to load data.")
    st.subheader("*Data Cleaning*")
    st.markdown("Expertise in using Pandas for cleaning, transforming, and preparing data for analysis.")
    st.subheader("*SQL*")
    st.markdown("Knowledge of MySQL for interacting with databases, querying data, and performing data cleaning and management tasks.")
    st.subheader("*Streamlit*")
    st.markdown("Ability to build interactive web applications using Streamlit for visualizing data and providing user-friendly interfaces.")
    st.header("*Developed by Devapriya M*")


#Slecting States & routes
df_a = pd.read_csv(r"red bus project/df_A.csv")
list_A = df_a["route_names"].tolist()

df_as = pd.read_csv(r"C:\Users\devap\OneDrive\Desktop\Scraping file\red bus project\df_As.csv")
list_AS= df_as["route_names"].tolist()

df_g = pd.read_csv(r"C:\Users\devap\OneDrive\Desktop\Scraping file\red bus project\df_G.csv")
list_G = df_g["route_names"].tolist()

df_h = pd.read_csv(r"C:\Users\devap\OneDrive\Desktop\Scraping file\red bus project\df_H.csv")
list_H= df_h["route_names"].tolist()

df_k = pd.read_csv(r"C:\Users\devap\OneDrive\Desktop\Scraping file\red bus project\df_K.csv")
list_K = df_k["route_names"].tolist()

df_r = pd.read_csv(r"C:\Users\devap\OneDrive\Desktop\Scraping file\red bus project\df_R.csv")
list_R = df_r["route_names"].tolist()

df_s = pd.read_csv(r"C:\Users\devap\OneDrive\Desktop\Scraping file\red bus project\df_S.csv")
list_S = df_s["route_names"].tolist()

df_t = pd.read_csv(r"C:\Users\devap\OneDrive\Desktop\Scraping file\red bus project\df_T.csv")
list_T = df_t["route_names"].tolist()

df_u = pd.read_csv(r"C:\Users\devap\OneDrive\Desktop\Scraping file\red bus project\df_U.csv")
list_U = df_u["route_names"].tolist()

df_w = pd.read_csv(r"C:\Users\devap\OneDrive\Desktop\Scraping file\red bus project\df_W.csv")
list_W = df_w["route_names"].tolist()

# connecting sql table
cursor.execute("select * from RED_BUS_DETAILS2")
data=cursor.fetchall()
column_names = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data=data,columns=column_names)



if page == "States & Routes":
    st.title("*Filtering Bus Details*")
    state_list = [
        "Andhra Pradesh", "Kerala", "Assam", "Goa", "Himachal Pradesh",
        "Rajasthan", "South Bengal", "West Bengal", "Uttar Pradesh", "Telangana"
    ]
    sl = st.selectbox("**List of States**", state_list)
 
#Selecting Andhra pradesh code  
    if sl == "Andhra Pradesh":
        k = st.selectbox("**Select Route**", list_A)
        route_data = df[df['Route_name'] == k]
#input for price & seatavilable        
        price = st.number_input("**Price**",min_value=400,max_value=5000, step=100)
        seat_available = st.number_input("**Seat Available**", min_value=1, max_value=50, step=1)
#database on user input
        filtered_data = route_data[
        (route_data["Price"] <= price) &
        (route_data['Seatavailable'] >= seat_available)
    ]
        st.write(filtered_data)

    
    if sl == "Kerala":
        K= st.selectbox("**List of Routes**",list_K)
        route_data = df[df['Route_name'] == K]
        
#input for price & seatavilable        
        price = st.number_input("**Price**",min_value=200,max_value=5000, step=100)
        seat_available = st.number_input("**Seat Available**", min_value=1, max_value=50, step=1)
#database on user input
        filtered_data = route_data[
        (route_data["Price"] <= price) &
        (route_data['Seatavailable'] >= seat_available)
    ]
        st.write(filtered_data)

    if sl == "Assam":
        k= st.selectbox("**List of Routes**",list_AS)
        route_data = df[df['Route_name'] == k]
        
#input for price & seatavilable        
        price = st.number_input("**Price**",min_value=200,max_value=5000, step=100)
        seat_available = st.number_input("**Seat Available**", min_value=1, max_value=50, step=1)
#database on user input
        filtered_data = route_data[
        (route_data["Price"] <= price) &
        (route_data['Seatavailable'] >= seat_available)
    ]
        st.write(filtered_data)

    if sl == "Goa":
        k= st.selectbox("**List of Routes**",list_G)
        route_data = df[df['Route_name'] == k]
        
#input for price & seatavilable        
        price = st.number_input("**Price**",min_value=200,max_value=5000, step=100)
        seat_available = st.number_input("**Seat Available**", min_value=1, max_value=50, step=1)
#database on user input
        filtered_data = route_data[
        (route_data["Price"] <= price) &
        (route_data['Seatavailable'] >= seat_available)
    ]
        st.write(filtered_data)

    if sl == "Himachal Pradesh":
       k= st.selectbox("**List of Routes**",list_H)
       route_data = df[df['Route_name'] == k]
        
#input for price & seatavilable        
       price = st.number_input("**Price**",min_value=200,max_value=5000, step=100)
       seat_available = st.number_input("**Seat Available**", min_value=1, max_value=50, step=1)
#database on user input
       filtered_data = route_data[
        (route_data["Price"] <= price) &
        (route_data['Seatavailable'] >= seat_available)
    ]
       st.write(filtered_data) 

    if sl == "Rajasthan":
       k= st.selectbox("**List of Routes**",list_R)
       route_data = df[df['Route_name'] == k]
        
#input for price & seatavilable        
       price = st.number_input("**Price**",min_value=200,max_value=5000, step=100)
       seat_available = st.number_input("**Seat Available**", min_value=1, max_value=50, step=1)
#database on user input
       filtered_data = route_data[
        (route_data["Price"] <= price) &
        (route_data['Seatavailable'] >= seat_available)
    ]
       st.write(filtered_data)          

    if sl == "South Bengal":
       k= st.selectbox("**List of Routes**",list_S)
       route_data = df[df['Route_name'] == k]
        
#input for price & seatavilable        
       price = st.number_input("**Price**",min_value=200,max_value=5000, step=100)
       seat_available = st.number_input("**Seat Available**", min_value=1, max_value=50, step=1)
#database on user input
       filtered_data = route_data[
        (route_data["Price"] <= price) &
        (route_data['Seatavailable'] >= seat_available)
    ]
       st.write(filtered_data)                 


    if sl == "West Bengal":
       k= st.selectbox("**List of Routes**",list_W)
       route_data = df[df['Route_name'] == k]
        
#input for price & seatavilable        
       price = st.number_input("**Price**",min_value=200,max_value=5000, step=100)
       seat_available = st.number_input("**Seat Available**", min_value=1, max_value=50, step=1)
#database on user input
       filtered_data = route_data[
        (route_data["Price"] <= price) &
        (route_data['Seatavailable'] >= seat_available)
    ]
       st.write(filtered_data) 

    if sl == "Uttar Pradesh":
       k= st.selectbox("**List of Routes**",list_U)
       route_data = df[df['Route_name'] == k]
        
#input for price & seatavilable        
       price = st.number_input("**Price**",min_value=200,max_value=5000, step=100)
       seat_available = st.number_input("**Seat Available**", min_value=1, max_value=50, step=1)
#database on user input
       filtered_data = route_data[
        (route_data["Price"] <= price) &
        (route_data['Seatavailable'] >= seat_available)
    ]
       st.write(filtered_data)     

    if sl == "Telangana":
       k= st.selectbox("**List of Routes**",list_T)
       route_data = df[df['Route_name'] == k]
        
#input for price & seatavilable        
       price = st.number_input("**Price**",min_value=200,max_value=5000, step=100)
       seat_available = st.number_input("**Seat Available**", min_value=1, max_value=50, step=1)
#database on user input
       filtered_data = route_data[
        (route_data["Price"] <= price) &
        (route_data['Seatavailable'] >= seat_available)
    ]
       st.write(filtered_data)  
