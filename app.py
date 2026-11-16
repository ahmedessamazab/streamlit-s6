from calendar import c
from os import name

import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")

st.title("Ahmed Azab's portfolio")

st.image(
    "./images/cat.webp",
    width=400,
)

st.write("Welcome to my Streamlit app!")

name = st.text_input("What is your name?")
age = st.slider("What is your age?", 0, 100, 25)

if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old.")


df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4, 5],
    'Column 2': ['A', 'B', 'C', 'D', 'E']
})

st.dataframe(df)
