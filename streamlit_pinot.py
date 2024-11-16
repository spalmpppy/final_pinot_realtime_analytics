import pinotdb
import pandas as pd
import streamlit as st
import altair as alt

# Connect to PinotDB
conn = pinotdb.connect(host='54.255.209.170', port=8099, path='/query/sql', scheme='http')

# Function to fetch data from Pinot
def fetch_data(query):
    return pd.read_sql(query, conn)

# Refresh interval in seconds
refresh_interval = st.sidebar.slider("Set Refresh Interval (seconds)", min_value=5, max_value=60, value=10)

st.title ("Real Time Visulization and Analytics Dashboard")