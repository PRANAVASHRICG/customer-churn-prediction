import streamlit as st
import joblib
import pandas as pd

model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction")

gender = st.selectbox("Gender", [0, 1])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", [0, 1])
Dependents = st.selectbox("Dependents", [0, 1])

tenure = st.number_input("Tenure", min_value=0, max_value=72, value=12)

PhoneService = st.selectbox("Phone Service", [0, 1])
MultipleLines = st.selectbox("Multiple Lines", [0, 1, 2])
InternetService = st.selectbox("Internet Service", [0, 1, 2])

OnlineSecurity = st.selectbox("Online Security", [0, 1, 2])
OnlineBackup = st.selectbox("Online Backup", [0, 1, 2])
DeviceProtection = st.selectbox("Device Protection", [0, 1, 2])
TechSupport = st.selectbox("Tech Support", [0, 1, 2])

StreamingTV = st.selectbox("Streaming TV", [0, 1, 2])
StreamingMovies = st.selectbox("Streaming Movies", [0, 1, 2])

Contract = st.selectbox("Contract", [0, 1, 2])
PaperlessBilling = st.selectbox("Paperless Billing", [0, 1])

PaymentMethod = st.selectbox("Payment Method", [0, 1, 2, 3])

MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0)

if st.button("Predict"):
    data = pd.DataFrame(
        [[
            gender,
            SeniorCitizen,
            Partner,
            Dependents,
            tenure,
            PhoneService,
            MultipleLines,
            InternetService,
            OnlineSecurity,
            OnlineBackup,
            DeviceProtection,
            TechSupport,
            StreamingTV,
            StreamingMovies,
            Contract,
            PaperlessBilling,
            PaymentMethod,
            MonthlyCharges,
            TotalCharges
        ]],
        columns=[
            'gender',
            'SeniorCitizen',
            'Partner',
            'Dependents',
            'tenure',
            'PhoneService',
            'MultipleLines',
            'InternetService',
            'OnlineSecurity',
            'OnlineBackup',
            'DeviceProtection',
            'TechSupport',
            'StreamingTV',
            'StreamingMovies',
            'Contract',
            'PaperlessBilling',
            'PaymentMethod',
            'MonthlyCharges',
            'TotalCharges'
        ]
    )

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer is likely to Churn")
    else:
        st.success("Customer is likely to Stay")
