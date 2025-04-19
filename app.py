import streamlit as st
import pandas as pd

df = pd.read_csv("1834_kazan.csv")
st.set_page_config(layout="wide")
st.title("Historical Data Viewer")
#st.dataframe(df)

search = st.text_input("Search")
filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]
st.dataframe(filtered_df)
