import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("model.pkl")

st.title("House Price Prediciton App")

st.divider()

st.write("This app uses machine Learning for prediction house price with give feature of the house. For using this app you can enter the inputs from this UI and then use predict button.")

st.divider()

bedrooms = st.number_input("Number of bedrooms", min_value = 0, value = 0)
bathrooms = st.number_input("Number of bathrooms", min_value = 0, value = 0)
livingarea = st.number_input("Living area", min_value = 0, value = 2000)
condition = st.number_input("Contition", min_value = 0, value = 3)
numberofschools = st.number_input("Number of schools", min_value = 0, value = 0)

st.divider()

X = [[bedrooms,bathrooms,livingarea,condition,numberofschools]]

prediction = st.button("Predict!")

if prediction:
    X_array = np.array(X)

    prediction = model.predict(X_array)[0]

    st.write(f"Prie prediction is {prediction:,.2f}")

else :
    st.write("Please use predict button after entering values")