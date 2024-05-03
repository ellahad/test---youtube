import joblib

# Function to load the sentiment analysis model
def load_model():
    return joblib.load('svm_classifier.joblib')

# Function to predict sentiment
def predict_sentiment(model, lemmatized_text):
    # Perform prediction using the model
    prediction = model.predict([lemmatized_text])
    return prediction[0]
