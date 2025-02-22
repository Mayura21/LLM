import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb # type: ignore
from tensorflow.keras.preprocessing import sequence # type: ignore
from tensorflow.keras.models import load_model # type: ignore

# 1. Load the imd dataset word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# Load model
model = load_model('14_DL_Simple_RNN/simple_rnn_imdb.h5')

# 2. Helper function to decode the review
def decode_review(encoded_review):
    return " ".join([reverse_word_index.get(i - 3, '?') for i in encoded_review])


# Function to preprocess user input
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review


# Streamlit app
import streamlit as st

st.title("IMDB Movie Review Sentiment Analysis")
st.write('Enter a movie review to clasify it as postive or negative.')


# User input
user_input = st.text_area("Movie review")

if st.button('Classify'):
    preprocess_input = preprocess_text(user_input)

    # Maske prediction
    prediction = model.predict(preprocess_input)

    semtiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'

    # Display result
    st.write(f'Sentiment: {semtiment}')
    st.write(f'Prediction score: {prediction[0][0]}')

else:
    st.write("Please enter a movie review")