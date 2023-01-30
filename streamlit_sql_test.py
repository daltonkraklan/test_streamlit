import streamlit as st
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:9U7s0GjX%*dH*aQI3Bmf@localhost:3306/nba_api')

st.set_page_config(
    page_title = 'Test',
    layout = 'wide'

)

def pd_to_sql(df,table):
    df.columns = df.columns.str.strip()
    df.to_sql(
        name = table,
        con = engine,
        index = False,
        if_exists = 'replace'
    )

def pd_read_sql(table):
    df = pd.read_sql(table , engine)
    return df

df = pd_read_sql('today_preds')

st.header('hello')

st.dataframe(df)
