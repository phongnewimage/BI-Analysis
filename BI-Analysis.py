import json
import requests
import streamlit as st
import pandas as pd  # pip install pandas
import plotly.express as px
import base64  # Standard Python Module
from io import StringIO, BytesIO  # Standard Python Module
from PIL import Image
import sqlite3
import pyodbc
import sqlalchemy
from fast_to_sql import fast_to_sql as fts
from sqlalchemy import create_engine
import urllib
image = Image.open('D:/Python/Templates/NI.png')
#encoding="utf-8"
   #---Page
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
#Title
sql_title = "select Mã_Tên,Full_Name as 'Tên Kép',\
Tháng_Liền_Kề_Trước_Đó as 'Khóa Tháng Trước',Tháng_Hiện_Tại as 'Khóa Tháng Gần Nhất',\
Đại_Hội as 'Danh Hiệu Đã Vinh Danh',\
Tổng_DH as 'Danh Hiệu Xác Thực',Tổng_DH_Letter as 'DH(Dạng Chữ)',\
SS_Tháng_Liền_Kề as 'So Sánh 2 Tháng Gần Nhất',SS_ĐH as 'So Sánh Với Đại Hội',\
Phone,Email,\
Tỉnh,Vùng_Miền as 'Vùng Miền',\
G_Code 'Mã Galaxy',E3SC_Name as 'Nhóm 3Sao',\
E5SC_Name as 'Nhóm 5Sao' \
from Monthly_Titles where G_Code <> 'None'"
dat_title = pd.read_sql(sql_title,cnn)
dat_title = pd.DataFrame(dat_title)
#Level
sql_level = "select Com_ID as 'Mã',Name as 'Tên',\
Phone,Email,\
Province as 'Tỉnh Thành',Vùng_Miền as 'Vùng Miền',\
G_Code 'Mã Galaxy',E3SC_Name as 'Nhóm 3Sao',E5SC_Name as 'Nhóm 5Sao',\
T1_2023,T2_2023,T3_2023,T4_2023,T5_2023,T6_2023,T7_2023,T8_2023,T9_2023,T10_2023,T11_2023,T12_2023 \
from Monthly_Level where G_Code <> 'None'"
dat_level = pd.read_sql(sql_level,cnn)
dat_level = pd.DataFrame(dat_level)
#Com
sql_com = "select Com_ID as 'Mã',Name as 'Tên',\
Phone,Email,\
Province as 'Tỉnh Thành',Vùng_Miền as 'Vùng Miền',\
G_Code 'Mã Galaxy',E3SC_Name as 'Nhóm 3Sao',E5SC_Name as 'Nhóm 5Sao',\
T1_2023,T2_2023,T3_2023,T4_2023,T5_2023,T6_2023,T7_2023,T8_2023,T9_2023,T10_2023,T11_2023,T12_2023,\
Q1_2023,Q2_2023,Q3_2023 \
from Monthly_Commission where G_Code <> 'None'"
dat_com = pd.read_sql(sql_com,cnn)
dat_com = pd.DataFrame(dat_com)
#Full_Com
sql_fullcom = "select Mã_Tên,Full_Name as 'Tên Kép',\
Tổng_DH_Letter as 'DH(Dạng Chữ)',Phone,Email,G_Code as 'Mã Galaxy',\
Tỉnh,Vùng_Miền as 'Vùng Miền',\
E3SC_Name as 'Nhóm 3Sao',E5SC_Name as 'Nhóm 5Sao',\
Commission as 'Hoa Hồng Tháng',Q_Com as 'Hoa Hồng Quý' \
from History_Commission where G_Code <> 'None'"
dat_fullcom = pd.read_sql(sql_fullcom,cnn)
dat_fullcom = pd.DataFrame(dat_fullcom)
#Com Analysis
sql_mlm = "select Mã_Tên,Full_Name as 'Mã_Kép',\
Tol_Com as 'Tổng Thu Nhập Trong Năm',Avg_Com as 'Thu Nhập Trung Bình Tháng',\
Best_Com as 'Thu Nhập Của Tháng Cao Nhất',Worst_Com as 'Thu Nhập Của Tháng Thấp Nhất',\
Having_Count as 'Số Tháng Có Thu Nhập',Tháng_Liền_Kề_Trước_Đó as 'Khóa Tháng Trước',\
Tháng_Hiện_Tại as 'Khóa Tháng Gần Nhất',Đại_Hội as 'Danh Hiệu Đã Vinh Danh',\
Tổng_DH as 'Danh Hiệu Xác Thực',Tổng_DH_Letter as 'DH(Dạng Chữ)',\
SS_Tháng_Liền_Kề as 'So Sánh 2 Tháng Gần Nhất',SS_ĐH as 'So Sánh Với Đại Hội',\
Phone,Email,\
Tỉnh,Vùng_Miền as 'Vùng Miền',\
G_Code 'Mã Galaxy',E3SC_Name as 'Nhóm 3Sao',\
E5SC_Name as 'Nhóm 5Sao' \
from Monthly_MLM where G_Code <> 'None'"
dat_mlm = pd.read_sql(sql_mlm,cnn)
dat_mlm = pd.DataFrame(dat_mlm)
#MainPage
st.set_page_config(page_title="New Image Sale-Data",page_icon=":tada:",layout="wide")
    #----Header
with open(r'D:\Python\Others\lottie\business.json',encoding='utf-8') as b:
 lottie_business = json.load(b)
with st.columns(5)[-1]:
     st.image(image)
with st.container():
    st.subheader("Hi, I am Phong :wave:")
    st.title("Business Analyst From New Image")
    st.write("I am happy to help you figure out something from my role to be more effective in our businesses :chart_with_upwards_trend:")
    st.write("Phone : 0933 731709")
    st.write("Email : phong.nguyenthanh@newimageasia.vn")
    st.write("My Power BI Project : https://app.powerbi.com/home?redirectedFromSignup=1&ScenarioId=Signup&redirectedWaitSimple=1")
    st.write("My Streamlit WebApp Project : http://10.84.19.38:8501")
    st.write("My Rate of New Member Buying Project : file:///D:/Python/Jupyter%20Notebook/Rate%20of%20New-Buying%20Analysis.html")
    st.write("Address : 04 Nguyen Dinh Chieu, DaKao Ward, District 1, Ho Chi Minh City, VietNam :flag-vn:")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("DANH HIỆU")
        st.write("##")
df_title = pd.DataFrame(dat_title)
st.table(df_title)
    #---Image
cnn.commit()
cnn.close()
