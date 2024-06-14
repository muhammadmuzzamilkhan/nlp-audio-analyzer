import streamlit as st
import tempfile
import os
import google.generativeai as genai
from dotenv import load_dotenv
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load environment variables
load_dotenv()

# Configure Google API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Download VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

def summarize_audio(audio_file_path):
    """Summarize the audio using Google's Generative API."""
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    audio_file = genai.upload_file(path=audio_file_path)
    response = model.generate_content(
        [
            "Please summarize the following audio.",
            audio_file
        ]
    )
    
    # Print the response structure for debugging
    # st.write("API Response:", response)
    
    if response and response.candidates:
        # Extract the summary text from the nested structure
        return response.candidates[0].content.parts[0].text
    else:
        raise ValueError("No valid response returned from the API. Please check the API key and input.")

def extract_keywords(text, num_keywords=10):
    """Extract keywords from the text."""
    vectorizer = CountVectorizer(stop_words='english', max_features=num_keywords)
    word_counts = vectorizer.fit_transform([text])
    keywords = vectorizer.get_feature_names_out()
    word_frequencies = np.asarray(word_counts.sum(axis=0)).flatten()
    keyword_freq = dict(zip(keywords, word_frequencies))
    sorted_keywords = sorted(keyword_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_keywords

def analyze_sentiment(text):
    """Analyze sentiment of the text."""
    scores = sid.polarity_scores(text)
    return scores

def save_uploaded_file(uploaded_file):
    """Save uploaded file to a temporary file and return the path."""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            return tmp_file.name
    except Exception as e:
        st.error(f"Error handling uploaded file: {e}")
        return None

# Streamlit app interface
st.title('Audio Summarization App with Keywords and Sentiment Analysis')

with st.expander("About this app"):
    st.write("""
        This app uses Google's generative AI to summarize audio files, extract keywords, 
        and perform sentiment analysis. Upload your audio file in WAV or MP3 format 
        and get a concise summary of its content along with key terms and sentiment scores.
    """)

audio_file = st.file_uploader("Upload Audio File", type=['wav', 'mp3'])
if audio_file is not None:
    audio_path = save_uploaded_file(audio_file)  # Save the uploaded file and get the path
    st.audio(audio_path)

    if st.button('Summarize Audio'):
        with st.spinner('Summarizing...'):
            try:
                summary_text = summarize_audio(audio_path)
                st.markdown("### Summary")
                st.info(summary_text)
                
                # Keyword Extraction
                st.markdown("### Extracted Keywords")
                keywords = extract_keywords(summary_text)
                keyword_text = ", ".join([f"**{keyword}** ({freq})" for keyword, freq in keywords])
                st.write(keyword_text)

                # Sentiment Analysis
                st.markdown("### Sentiment Analysis")
                sentiment_scores = analyze_sentiment(summary_text)
                st.write(f"**Negative Sentiment:** {sentiment_scores['neg']*100:.2f}%")
                st.write(f"**Neutral Sentiment:** {sentiment_scores['neu']*100:.2f}%")
                st.write(f"**Positive Sentiment:** {sentiment_scores['pos']*100:.2f}%")
                st.write(f"**Overall Sentiment (Compound Score):** {sentiment_scores['compound']}")
            except ValueError as e:
                st.error(f"Error: {e}")