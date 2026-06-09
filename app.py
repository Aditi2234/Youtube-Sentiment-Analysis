import streamlit as st
import os
from dotenv import load_dotenv
from sentiment_analysis import fetch_clean_analyze_comments
load_dotenv()

def main():
    st.title('YouTube Comment Sentiment Analysis')

    # Input video URL
    video_url = st.text_input("Enter YouTube Video URL")

    if video_url:
        # Fetch, clean, and analyze comments
        fig_bar, fig_pie = fetch_clean_analyze_comments(video_url)
        
        # Display the sentiment distribution as bar and pie charts
        st.subheader('Sentiment Distribution (Bar Chart)')
        st.plotly_chart(fig_bar)

        st.subheader('Sentiment Distribution (Pie Chart)')
        st.plotly_chart(fig_pie)

if __name__ == "__main__":
    main()
