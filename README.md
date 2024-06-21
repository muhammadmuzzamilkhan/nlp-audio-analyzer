# NLP Audio Analyzer

![NLP Audio Analyzer](https://via.placeholder.com/1000x200.png?text=NLP+Audio+Analyzer)

## Overview

**NLP Audio Analyzer** is a Streamlit web application that allows users to upload audio files in WAV or MP3 format, summarizes the content, extracts keywords, and performs sentiment analysis on the summary. This app leverages Google's Generative AI and Natural Language Processing (NLP) techniques to provide meaningful insights from audio files.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Getting Your Google API Key](#getting-your-google-api-key)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Audio Summarization**: Summarizes the provided audio file using Google's Generative AI.
- **Keyword Extraction**: Extracts key terms from the summarized text.
- **Sentiment Analysis**: Analyzes the sentiment of the summarized text using VADER sentiment analysis.

## Installation

### Prerequisites

- Python 3.7+
- Streamlit
- Google API Key (with access to Google's Generative AI)

### Steps

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/nlp-audio-analyzer.git
    cd nlp-audio-analyzer
    ```

2. **Create and activate a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the environment variables**

    Create a `.env` file in the project root directory and add your Google API key:

    ```dotenv
    GOOGLE_API_KEY = 'YOUR_GOOGLE_API_KEY_HERE'
    ```

5. **Run the application**

    ```bash
    streamlit run app.py
    ```

6. Open your browser and navigate to `http://localhost:8501`

## Usage

1. **Upload Audio File**

    - Click on "Upload Audio File" button to upload your audio file in WAV or MP3 format.

2. **Summarize Audio**

    - After uploading the audio file, click on "Summarize Audio" button.
    - The app will process the audio and display the summary, extracted keywords, and sentiment analysis.

## Getting Your Google API Key

To use Google's Generative AI services, you need to obtain an API key. Here are the steps to get your API key:

1. **Go to the Google Cloud Console**

    Navigate to the [Google Cloud Console](https://console.cloud.google.com/).

2. **Create a New Project**

    - Click on the project dropdown at the top of the page and select "New Project".
    - Enter a name for your project and click "Create".

3. **Enable APIs and Services**

    - In the left-hand menu, navigate to "APIs & Services" > "Library".
    - Search for the "Generative Language API" and click on it.
    - Click "Enable" to enable the API for your project.

4. **Create API Credentials**

    - Navigate to "APIs & Services" > "Credentials".
    - Click "Create Credentials" and select "API Key".
    - Copy the API key displayed in the popup.

5. **Add API Key to .env File**

    - Open the `.env` file in your project root directory.
    - Add your API key to the `GOOGLE_API_KEY` variable.

    ```dotenv
    GOOGLE_API_KEY = 'YOUR_GOOGLE_API_KEY_HERE'
    ```

## Project Structure

  ```structure
  nlp-audio-analyzer/
  │
  ├── venv2/
  ├── .env
  ├── LICENSE
  ├── README.md
  ├── app.py
  ├── requirements.txt
  ```

### Main Files

- **app.py**: Contains the Streamlit app code that handles audio file upload, summarization, keyword extraction, and sentiment analysis.

### Key Functions

- `summarize_audio(audio_file_path)`: Summarizes the audio using Google's Generative AI.
- `extract_keywords(text, num_keywords=10)`: Extracts keywords from the summarized text.
- `analyze_sentiment(text)`: Analyzes the sentiment of the summarized text.
- `save_uploaded_file(uploaded_file)`: Saves the uploaded file to a temporary location.

## Contributing

1. **Fork the repository**
2. **Create a new branch for your feature or bugfix**

    ```bash
    git checkout -b feature-name
    ```

3. **Make your changes**
4. **Commit your changes**

    ```bash
    git commit -m "Description of your changes"
    ```

5. **Push to your branch**

    ```bash
    git push origin feature-name
    ```

6. **Submit a pull request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: Remember to replace placeholders such as `YOUR_GOOGLE_API_KEY_HERE` and the URL in the clone command with actual values relevant to your project.
