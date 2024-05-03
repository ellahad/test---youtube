from flask import Flask, render_template, request
from preprocessing import clean_text, tokenize_and_remove_stopwords, lemmatize_tokens
from modeling import load_model, predict_sentiment

app = Flask(__name__)

# Load the sentiment analysis model
model = load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the user input from the form
    user_input = request.form['user_input']
    
    # Clean, tokenize, and lemmatize the user input
    cleaned_text = clean_text(user_input)
    tokenized_text = tokenize_and_remove_stopwords(cleaned_text)
    lemmatized_text = lemmatize_tokens(tokenized_text)
    
    # Predict sentiment using the model
    sentiment = predict_sentiment(model, lemmatized_text)
    
    return render_template('result.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
