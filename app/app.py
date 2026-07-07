import streamlit as st
import numpy as np
import joblib
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)


lr_model = joblib.load(
    os.path.join(MODEL_DIR,"logistic_regression.pkl")
)

svm_model = joblib.load(
    os.path.join(MODEL_DIR,"svm_model.pkl")
)

nn_model = joblib.load(
    os.path.join(MODEL_DIR,"nn_model.pkl")
)

scaler = joblib.load(
    os.path.join(MODEL_DIR,"scaler.pkl")
)



st.title(
"Diabetes Prediction System"
)
st.info(
"""
This project is a diabetes risk prediction system based on machine learning models.

This prediction is not a medical diagnosis and does not provide %100 accurate results.
For the most reliable prediction performance, selecting the Neural Network model is recommended.

Please consult a healthcare professional for medical decisions.
"""
)


model_name = st.selectbox(
"Choose Model",
[
"Logistic Regression",
"SVM",
"Neural Network"
]
)



preg = st.number_input("Pregnancies")

glu = st.number_input("Glucose")

bp = st.number_input("Blood Pressure")

skin = st.number_input("Skin Thickness")

ins = st.number_input("Insulin")

bmi = st.number_input("BMI")

dpf = st.number_input(
"Diabetes Pedigree Function"
)

age = st.number_input("Age")



if st.button("Predict"):


    data = np.array(
    [[
    preg,
    glu,
    bp,
    skin,
    ins,
    bmi,
    dpf,
    age,

    int(glu==0),
    int(bp==0),
    int(skin==0),
    int(ins==0),
    int(bmi==0)

    ]]
    )


    data = scaler.transform(data)


    if model_name=="Logistic Regression":

        result = lr_model.predict(data)


    elif model_name=="SVM":

        result = svm_model.predict(data)


    else:

        result = nn_model.predict(data)



    if result[0]==1:

        st.error(
        "Diabetes Detected"
        )

    else:

        st.success(
        "No Diabetes"
        )