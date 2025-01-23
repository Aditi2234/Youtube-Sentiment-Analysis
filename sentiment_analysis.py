from googleapiclient.discovery import build
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
import plotly.graph_objects as go

# YouTube API setup
API_KEY = 'API_KEY' 
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def fetch_clean_analyze_comments(video_url):
    video_id = video_url.split('v=')[-1]
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

    # Fetch all comments
    comments = []
    next_page_token = None

    while True:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,  
            textFormat="plainText",
            pageToken=next_page_token
        )
        response = request.execute()
        
        # Append the comments to the list
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        
        # Check if there are more comments (pagination)
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break  

    # Clean comments
    def clean_text(text):
        text = re.sub(r'http\S+', '', text)  
        text = re.sub(r'[^a-zA-Z\s]', '', text)  
        text = text.lower()  
        stop_words = set(stopwords.words('english'))
        text = ' '.join([word for word in text.split() if word not in stop_words])
        return text

    cleaned_comments = [clean_text(comment) for comment in comments]

    # Perform sentiment analysis using VADER
    sid = SentimentIntensityAnalyzer()
    sentiments = []
    for comment in cleaned_comments:
        sentiment_scores = sid.polarity_scores(comment)
        if sentiment_scores['compound'] > 0.05:
            sentiments.append('Positive')
        elif sentiment_scores['compound'] < -0.05:
            sentiments.append('Negative')
        else:
            sentiments.append('Neutral')

    sentiment_counts = { 'Positive': sentiments.count('Positive'),
                         'Negative': sentiments.count('Negative'),
                         'Neutral': sentiments.count('Neutral') }

    # Generate Bar Chart
    fig_bar = go.Figure(data=[go.Bar(x=list(sentiment_counts.keys()), 
                                    y=list(sentiment_counts.values()), 
                                    marker=dict(color=['green', 'red', 'gray']))])
    fig_bar.update_layout(
        title="Sentiment Distribution of YouTube Comments",
        xaxis_title="Sentiment",
        yaxis_title="Number of Comments",
        template="plotly"
    )

    # Generate Pie Chart
    fig_pie = go.Figure(data=[go.Pie(labels=list(sentiment_counts.keys()), 
                                     values=list(sentiment_counts.values()), 
                                     hole=0.3)])
    fig_pie.update_layout(title_text="Sentiment Distribution of YouTube Comments")

    return fig_bar, fig_pie



