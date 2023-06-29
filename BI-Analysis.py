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
#---SQL---
sql = "select Segment,\
sum(case when Segment is not null then 1 else 0 end) as SL \
from \
(select ID,Name,Register_Card,Min(Buying_Month) as Buying_Month,\
(case when Min(Buying_Month) - Register_Card = 0 then 'At1stMonth' \
when Min(Buying_Month) - Register_Card = 1 then 'At2ndMonth' \
when Min(Buying_Month) - Register_Card = 2 then 'At3rdMonth' \
when Min(Buying_Month) - Register_Card = 3 then 'At4thMonth' \
when Min(Buying_Month) - Register_Card = 4 then 'At5thMonth' \
when Min(Buying_Month) - Register_Card = 5 then 'At6thMonth' \
when Min(Buying_Month) - Register_Card = 6 then 'At7thMonth' \
when Min(Buying_Month) - Register_Card = 7 then 'At8thMonth' \
when Min(Buying_Month) - Register_Card = 8 then 'At9thMonth' \
when Min(Buying_Month) - Register_Card = 9 then 'At10thMonth' \
when Min(Buying_Month) - Register_Card = 10 then 'At11tMonth' \
when Min(Buying_Month) - Register_Card = 11 then 'At12thMonth' else 'None' end) as Segment,Amt23 \
from \
(select Customer_ID as ID,Name,\
N_Month as Register_Card,\
Month as Buying_Month,\
Amt,Amt_New,\
(case when Month = N_Month and Amt > Amt_New then 'At First Month' else 'Not At First Month' end) as 'Term-1',\
(case when Month >= N_Month and Amt > Amt_New then 'Buy' \
else 'None-Buy' end) as 'Term-2' \
from \
(select Customer_ID,Month,\
cast(sum(Summary) as int) as Amt \
from Master_Sale \
where Year = 2023 and Month <= 5 \
group by Customer_ID,Month) as full_sale \
left join \
(select Customer_ID as ID,Month as N_Month,\
cast(sum(Summary) as int) as Amt_New \
from Master_Sale \
where Product_code = '101' and Year = 2023 and Month <= 5 \
group by Customer_ID,Month) as new_sale on \
Customer_ID = ID \
left join Master_NPP on \
Customer_ID = D_ID \
where N_Month is not null and \
(case when Month >= N_Month and Amt > Amt_New then 'Buy' \
else 'None-Buy' end) = 'Buy') as Final_Data \
left join (select Customer_ID,\
cast(sum(Summary) as int) as Amt23 \
from Master_Sale \
where Month <= 5 and Year = 2023 \
group by Customer_ID) as Total_Sale on \
ID = Customer_ID \
group by ID,Name,Register_Card,Amt23) as FN_sale \
group by Segment \
order by SL DESC"
df = pd.read_sql(sql,cnn)
df = pd.DataFrame(df)
df['Rate'] = ((df['SL']/17913)*100).round(2)
df = pd.DataFrame(df)
st.write(df)
