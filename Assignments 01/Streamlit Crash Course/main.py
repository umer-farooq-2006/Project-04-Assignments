import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df)

    st.write("Basic Statistics:")
    st.write(df.describe())

    st.write("Column Selector")
    column = st.selectbox("Choose a column", df.columns)
    st.line_chart(df[column])
