import streamlit as st
import pandas as pd
import sqlalchemy
import mysql.connector

cnx  = mysql.connector.connect(
    host = "45.79.146.41",
    user = 'krakman',
    passwd = 'H0stAdm1n123!',
    database = 'nba_api'
)

st.set_page_config(
    page_title = 'Test',
    layout = 'wide'
)

cursor = cnx.cursor()

df = pd.read_sql(
    sql = 'SELECT * FROM adv_stats_archive',
    con = cnx
)

st.dataframe(df)
