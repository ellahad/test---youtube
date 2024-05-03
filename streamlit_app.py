import streamlit as st
import pandas as pd
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Function to analyze sentiment using TextBlob
def analyze_textblob_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Function to analyze sentiment using VADER
def analyze_vader_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = analyzer.polarity_scores(text)
    return sentiment_dict['compound']

# Function to fetch comments from a YouTube video
def fetch_youtube_comments(api_key, video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100  # Adjust as needed
    ).execute()
    comments = [item['snippet']['topLevelComment']['snippet']['textDisplay'] for item in response['items']]
    return comments

# Function to tokenize text and remove stopwords
def tokenize_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    return filtered_words

# Streamlit app
def main():
    st.title("YouTube Sentiment Analysis")

    # Input fields for API key and YouTube video ID
    api_key = st.text_input("Enter Your YouTube API Key")
    video_id = st.text_input("Enter YouTube Video ID (e.g., dQw4w9WgXcQ)")

    # Button to fetch comments
    if st.button("Fetch Comments"):
        if not api_key:
            st.warning("Please enter your YouTube API key.")
        elif not video_id:
            st.warning("Please enter a YouTube video ID.")
        else:
            st.info("Fetching comments...")
            try:
                comments = fetch_youtube_comments(api_key, video_id)
                st.success(f"Successfully fetched {len(comments)} comments.")
                st.write("Sample Comments:")
                st.write(pd.DataFrame(comments, columns=["Comment"]))
            except HttpError as e:
                st.error(f"Error fetching comments: {str(e)}")

    # Button to perform sentiment analysis
    if 'comments' in locals():
        if st.button("Perform Sentiment Analysis"):
            st.info("Performing sentiment analysis...")
            try:
                comment_df = pd.DataFrame(comments, columns=["Comment"])
                comment_df['TextBlob_Sentiment'] = comment_df['Comment'].apply(analyze_textblob_sentiment)
                comment_df['VADER_Sentiment'] = comment_df['Comment'].apply(analyze_vader_sentiment)

                # Calculate sentiment percentages
                textblob_counts = comment_df['TextBlob_Sentiment'].value_counts(normalize=True)
                vader_counts = comment_df['VADER_Sentiment'].value_counts(normalize=True)

                # Display sentiment analysis results
                st.success("Sentiment analysis completed.")
                st.write("Sentiment Analysis Results:")
                st.write("TextBlob Sentiment:")
                st.bar_chart(textblob_counts)
                st.write("VADER Sentiment:")
                st.bar_chart(vader_counts)

                # Tokenize comments and remove stopwords
                comment_df['Tokenized_Comment'] = comment_df['Comment'].apply(tokenize_text)

                # Filter comments based on sentiment
                positive_comments = comment_df[comment_df['VADER_Sentiment'] > 0]['Tokenized_Comment']
                negative_comments = comment_df[comment_df['VADER_Sentiment'] < 0]['Tokenized_Comment']
                neutral_comments = comment_df[comment_df['VADER_Sentiment'] == 0]['Tokenized_Comment']

                # Count most common words
                positive_word_counts = Counter([word for comment in positive_comments for word in comment])
                negative_word_counts = Counter([word for comment in negative_comments for word in comment])
                neutral_word_counts = Counter([word for comment in neutral_comments for word in comment])

                # Display most common words
                st.write("Most Common Words in Positive Comments:")
                st.write(positive_word_counts.most_common(10))

                st.write("Most Common Words in Negative Comments:")
                st.write(negative_word_counts.most_common(10))

                st.write("Most Common Words in Neutral Comments:")
                st.write(neutral_word_counts.most_common(10))
                
            except Exception as e:
                st.error(f"Error performing sentiment analysis: {str(e)}")

if __name__ == "__main__":
    main()
