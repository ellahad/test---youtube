from flask import Flask, render_template, request
from preprocessing import clean_text, tokenize_and_remove_stopwords, lemmatize_tokens
from modeling import load_model, predict_sentiment

app = Flask(YoutubeApp Analyzer)

# Route to display the form for entering YouTube channel information
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and display sentiment analysis results
@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the YouTube channel URL or ID from the form
    channel_url = request.form['channel_url']

    # Fetch comments from the YouTube channel using the YouTube Data API
    # Perform sentiment analysis on the comments
    # Identify common words in each sentiment category

    # Example data (replace with actual sentiment analysis results and common words)
    sentiment_results = {
        'positive': 60,
        'negative': 20,
        'neutral': 20
    }

    common_words = {
        'positive': ['great', 'awesome', 'love'],
        'negative': ['terrible', 'bad', 'disappointed'],
        'neutral': ['interesting', 'okay', 'average']
    }

    # Render the results template with the sentiment analysis results and common words
    return render_template('results.html', sentiment_results=sentiment_results, common_words=common_words)

if __name__ == '__main__':
    app.run(debug=True)
