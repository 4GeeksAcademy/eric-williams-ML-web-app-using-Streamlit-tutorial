import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'final_rf_model.joblib')
model = joblib.load(model_path)

# Title for your app
st.title('Store Sales Prediction Tool')

# Getting user input
st.header('Please enter the details:')
store_id = st.text_input('Store ID')
holiday = st.selectbox('Holiday (Yes or No)', ['No', 'Yes'])
order = st.text_input('Order Count')
day_of_week = st.text_input('Day of the Week')
month = st.text_input('Month')
store_type = st.selectbox('Store Type', ['S1', 'S2', 'S3', 'S4'])
location_type = st.selectbox('Location Type', ['L1', 'L2', 'L3', 'L4', 'L5'])
region_code = st.selectbox('Region Code', ['R1', 'R2', 'R3', 'R4'])
discount = st.selectbox('Discount', ['No', 'Yes'])

# Button to make prediction
if st.button('Predict Sales'):
    # Preparing data for prediction
    data = {
        'Store_id': int(store_id),
        'Holiday': 1 if holiday == 'Yes' else 0,
        '#Order': int(order),
        'Day_of_Week': int(day_of_week),
        'Month': int(month),
        'Store_Type_S1': 1 if store_type == 'S1' else 0,
        'Store_Type_S2': 1 if store_type == 'S2' else 0,
        'Store_Type_S3': 1 if store_type == 'S3' else 0,
        'Store_Type_S4': 1 if store_type == 'S4' else 0,
        'Location_Type_L1': 1 if location_type == 'L1' else 0,
        'Location_Type_L2': 1 if location_type == 'L2' else 0,
        'Location_Type_L3': 1 if location_type == 'L3' else 0,
        'Location_Type_L4': 1 if location_type == 'L4' else 0,
        'Location_Type_L5': 1 if location_type == 'L5' else 0,
        'Region_Code_R1': 1 if region_code == 'R1' else 0,
        'Region_Code_R2': 1 if region_code == 'R2' else 0,
        'Region_Code_R3': 1 if region_code == 'R3' else 0,
        'Region_Code_R4': 1 if region_code == 'R4' else 0,
        'Discount_No': 1 if discount == 'No' else 0,
        'Discount_Yes': 1 if discount == 'Yes' else 0
    }
    
    # Convert data into DataFrame for prediction
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    output = round(prediction[0], 2)
    
    # Display the prediction
    st.subheader(f'Predicted Store Sales: ${output}')

# Running the app
# To run the app, save this script as app.py and in the terminal run: streamlit run app.py