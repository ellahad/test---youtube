import streamlit as st
import pickle
import numpy as np

# Load your trained model
model = pickle.load(open('model.pkl', 'rb'))

# Define the app interface
st.title('Predictive Model App')
st.write('Enter the input data to get the prediction')

# Assuming we have one numerical input for the model
input_data = st.number_input('Enter input value')

# Button to make prediction
if st.button('Predict'):
    # Convert input to numpy array and reshape for the model
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)
    st.write(f'The prediction is: {prediction[0]}')

