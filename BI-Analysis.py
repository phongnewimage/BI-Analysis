import streamlit as st
import pandas as pd
import pyodbc
import sqlalchemy
from sqlalchemy import create_engine
import urllib
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
conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=HCM-SALES-LT-05;'
    r'DATABASE=Monthly_Report;'
    r'UID=sa;'
    r'PWD=Image2023;'
)
quoted = urllib.parse.quote_plus(conn_str)
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={quoted}')
cnn = engine.connect()
