# Youtube Sentiment Analysis

## Overview

This project analyzes the sentiments of comments on a given YouTube video in real-time. Using the YouTube Data API, it fetches comments, cleans the text, and performs sentiment analysis using the VADER sentiment analysis tool. The results are visualized as bar and pie charts using Plotly, and a user-friendly interface is provided via Streamlit.


## Key Features
1. Fetches comments from a YouTube video in real-time.
2. Cleans and preprocesses text data by removing special characters, links, and stopwords.
3. Performs sentiment analysis using VADER (Valence Aware Dictionary and Sentiment Reasoner).
4. Categorizes sentiments into Positive, Negative, and Neutral.
5. Visualizes sentiment distribution with interactive bar and pie charts.
6. Utilizes Streamlit to create a user-friendly web interface.

## Project Description
The YouTube Comment Sentiment Analysis project analyzes and visualizes YouTube video comment sentiments in real-time. Using the YouTube Data API, it fetches comments, preprocesses them by removing irrelevant content (e.g., special characters, URLs, and stopwords), and prepares them for sentiment analysis.

Sentiment analysis is conducted using VADER, a tool optimized for short, informal texts, categorizing sentiments into Positive, Negative, or Neutral. Results are presented interactively via Plotly bar and pie charts, offering a clear view of public sentiment.

The user-friendly interface, built with Streamlit, provides an easy way for content creators, analysts, and researchers to assess audience reactions, making the project ideal for analyzing sentiments on topics like politics, entertainment, or product reviews.
