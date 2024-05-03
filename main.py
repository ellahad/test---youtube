import pandas as pd
import streamlit as st
from clean_data import clean_data
from sentiment_analysis import analyze_sentiment_textblob, analyze_sentiment_vader
from word_cloud_generation import generate_word_cloud

# Load data
@st.cache
def load_data():
    # Load your dataset here
    pass

data = load_data()

# Perform data cleaning
cleaned_data = clean_data(data)

# Perform sentiment analysis
# Example using TextBlob
cleaned_data['Sentiment_TextBlob'] = cleaned_data['comment'].apply(analyze_sentiment_textblob)

# Example using VADER
cleaned_data['Sentiment_VADER'] = cleaned_data['comment'].apply(analyze_sentiment_vader)

# Generate word cloud
generate_word_cloud(cleaned_data['lemmatized_text'].str.cat(sep=' '))
