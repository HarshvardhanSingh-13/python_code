import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:",0,100,25)

st.write("Your age is",age)

if name:
    st.write(f"Hello {name}")

options = ["Python", "Java", "C++", "C#"]
choice = st.selectbox("Choose your Favourite Programming Language", options)
st.write(f"Your favourite language is {choice}")

uploaded_file = st.file_uploader("Hey Chose a CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)