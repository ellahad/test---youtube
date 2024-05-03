# This script contains code for data collection and preprocessing

# Import necessary libraries
from googleapiclient.discovery import build
import pandas as pd
import datetime
from bs4 import BeautifulSoup
import re
from langdetect import detect, LangDetectException

# Function to fetch video details by video ID
def fetch_video_details(video_id):
    # Implementation goes here

# Function to fetch videos uploaded by Marques Brownlee in the past 1 year
def fetch_videos():
    # Implementation goes here

# Fetch videos
videos = fetch_videos()

# Extract relevant statistics for each video
video_data = []
for video in videos:
    # Implementation goes here

# Convert to DataFrame
df = pd.DataFrame(video_data)

# Display descriptive statistics
df.describe()

# Getting the Top 10 Videos by view count
# Order the videos based on views from highest to lowest
df_sorted = df.sort_values(by='views', ascending=False)

# Display the top 10 videos
top_10_videos = df_sorted.head(10)
print("Top 10 Videos:")
top_10_videos

# Let's create a DataFrame
# Data as list of dictionaries
data = [
    # Sample data
]

df = pd.DataFrame(data)

# Display the DataFrame
df

# Save to CSV
df.to_csv('top_videos.csv', index=False)

# Function to fetch comments from YouTube videos
def fetch_comments(video_id):
    # Implementation goes here

# Use of Video IDs
video_ids = ['dtp6b76pMak', 'OFvXuyITwBI']

# Fetch comments for each video
all_comments = []
for video_id in video_ids:
    video_comments = fetch_comments(video_id)
    all_comments.extend(video_comments)

# Convert the list of comment dictionaries to a DataFrame
comments_df = pd.DataFrame(all_comments)

# Save the DataFrame to a CSV file
comments_df.to_csv('youtube_comments.csv', index=False)

# Data cleaning functions
# Implementation of clean_text, is_english, and other cleaning functions goes here

# Apply data cleaning functions
comments_df['cleaned_text'] = comments_df['comment_text'].apply(clean_text)
comments_df['is_english'] = comments_df['cleaned_text'].apply(is_english)
# Implementation goes here

# Save the cleaned DataFrame
comments_df.to_csv('clean_comments.csv', index=False)
