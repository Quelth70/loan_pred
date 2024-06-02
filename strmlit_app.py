import streamlit as st
import pickle
import numpy as np


st.title("Loaning Eligibility Prediction")

values = []

values.append(st.sidebar.number_input("Applicant Income", key = 1))
values.append(st.sidebar.number_input("Coapplicant Income", key = 2))
values.append(st.sidebar.number_input("Loan Amount", key = 3))
values.append(st.sidebar.number_input("Loan Amount Term", key = 4))
values.append(st.sidebar.number_input("Credit History", key = 5))
male = st.sidebar.selectbox("Male or Female?", ("Male", "Female"))
if male == "Male":
    values.append(1)
else:
    values.append(0)
married = st.sidebar.selectbox("Married?", ("Yes", "No"))
if married == "Yes":
    values.append(1)
else:
    values.append(0)
dependents = st.sidebar.selectbox("Dependents", ("0", "1", "2", "+3"))
if dependents == "0":
    values.extend([0, 0, 0])
elif dependents == "1":
    values.extend([1, 0, 0])
elif dependents == "2":
    values.extend([0, 1, 0])
else:
    values.extend([0, 0, 1])
graduated = st.sidebar.selectbox("Graduates?", ("Yes", "No"))
if graduated == "Yes":
    values.append(0)
else:
    values.append(1)
s_employed = st.sidebar.selectbox("Self employed?", ("Yes", "No"))
if s_employed == "Yes":
    values.append(1)
else:
    values.append(0)
prop_area = st.sidebar.selectbox("Property Area", ("Rural", "Semiurban", "Urban"))
if prop_area == "Rural":
    values.extend([0, 0])
elif prop_area == "Semiurban":
    values.extend([1, 0])
else:
    values.extend([0, 1])

feeding = np.array([values])

def load_model():
    with open("model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

model = load_model()
if st.sidebar.button("Predict"):
    y_pred = model.predict(feeding)
    st.write(f"The probability that this person will pay is: {model.predict_proba(feeding)[0,1]}")
    if y_pred[0] == 1:
        st.write(f"This person is eligible for a loan.")
    else:
        st.write(f"This person is not eligible for a loan.")
