import streamlit as st
import pandas as pd


st.title("Stramlit Text Input")

name = st.text_input("Enter your name: ")

age = st.slider("Select your age", 0, 100, 25)
st.write(f"Your age is {age}.")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favourite language", options=options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}")

data = {
    'Name': ["John", "Maaria", "Krish", "Raj"],
    'Age': [20, 25, 46, 34],
    'Ciry': ["New York", "Berlin", "London", "Bengaluru"]
}

df = pd.DataFrame(data=data)
df.to_csv('SampleData.csv')
st.write(df)

uploaded_file = st.file_uploader("Choose a csv file", type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)