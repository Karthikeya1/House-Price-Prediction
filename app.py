import streamlit as st
import joblib
import numpy as np

#Loading the model
model1=joblib.load("RandomForest.pkl")
model2=joblib.load("GradientBoost.pkl")
model3=joblib.load("XGBoost.pkl")
scalar=joblib.load("Scalar.pkl")

st.title("House Price Prediction")

#Taking the Inputs from the user
bed=st.number_input("Number of Bedrooms")
bath=st.number_input("Number of Bathrooms")
living_area=st.number_input("Living Area")
floors=st.number_input("Number of Floors")
waterfont=st.number_input("Water Font Present [0:No, 1: Yes]")
views=st.number_input("Number of Views")
grade=st.number_input("Grade of the house")
house=st.number_input("Area of the house (excluding basement)")
basement=st.number_input("Area of the basement")
renov_year=st.number_input("Renovation Year")
postal=st.number_input("Postal Code")
living=st.number_input("Living Area Renov")


#Prediction
if st.button("Predict"):
    data=np.array([[bed,bath,living_area,floors,waterfont,views,grade,house,basement,renov_year,postal,living]])
    transformed_data=scalar.transform(data)
    pred1=model1.predict(transformed_data)
    pred2=model2.predict(transformed_data)
    pred3=model3.predict(transformed_data)

    st.write("Random Forest Algorithm ",pred1)
    st.write("Gradient Boost Algorithm ",pred2)
    st.write("XGBoost Algorithm ",pred3)