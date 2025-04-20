import streamlit as st
import pandas as pd

df = pd.read_csv("1834_kazan.csv")
st.set_page_config(page_title="Список кантонистов", layout="wide")
st.title("Список кантонистов")

str_col_list = ['Ф1', 'И1', 'О1', 'Ф2', 'И2', 'О2', 'и2', 'о2']

# Create filters
filters = {}
with st.expander("Фильтры по колонкам"):
    for col in df.columns:
        if col in str_col_list:
            continue
        unique_vals = df[col].dropna().astype(str).unique()
        if unique_vals.size == 0:
            continue

        selected = st.multiselect(f"{col}", sorted(unique_vals))
        if selected:
            filters[col] = selected

search = st.text_input("Search")

# Apply filters
filtered_df = df.copy()
for col, selected_vals in filters.items():
    filtered_df = filtered_df[filtered_df[col].astype(str).isin(selected_vals)]

filtered_df = filtered_df[filtered_df.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]

st.dataframe(filtered_df)
