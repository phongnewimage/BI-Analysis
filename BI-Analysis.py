import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
#MainPage
st.set_page_config(page_title="NI Data Science",page_icon=":tada:",layout="wide")
    #----Header
with st.container():
    st.subheader("Hi, I am Phong :wave:")
    st.title("Business Analyst From New Image")
    st.write("I am happy to help you figure out something from my role to be more effective in our businesses :chart_with_upwards_trend:")
    st.write("Phone : 0933 731709")
    st.write("Email : phong.nguyenthanh@newimageasia.vn")
    st.write("My Power BI Project : https://app.powerbi.com/home?redirectedFromSignup=1&ScenarioId=Signup&redirectedWaitSimple=1")
    st.write("Address : 04 Nguyen Dinh Chieu, DaKao Ward, District 1, Ho Chi Minh City, VietNam :flag-vn:")
#---SQL---
st.read("file:///D:/Python/Jupyter%20Notebook/Rate%20of%20Lastest%20LogIn%20Analysis.html")
st.write('file:///D:/Python/Jupyter%20Notebook/Rate%20of%20Lastest%20LogIn%20Analysis.html')
