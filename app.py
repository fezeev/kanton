import streamlit as st
import pandas as pd

df = pd.read_csv("1834_kazan.csv")
st.set_page_config(page_title="Список кантонистов", layout="wide")
st.title("Список кантонистов")
search = st.text_input("Search")
filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]
st.dataframe(filtered_df)
