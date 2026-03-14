import pandas as pd
import joblib
import streamlit as st

# Load trained model
import os
import joblib

BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "model", "best_et_model.pkl")

model = joblib.load(model_path)
st.set_page_config(page_title="Credit Risk Predictor", page_icon="💳", layout="wide")
st.title("💳 Credit Risk Prediction")
st.write("Enter applicant's information to predict credit risk (1: Good, 0: Bad)")

# --- Input Fields in Columns ---
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=90, value=30)
    sex = st.selectbox("Sex", options=['female', 'male'])
    job = st.number_input("Job (0-3)", min_value=0, max_value=3, value=1)
    housing = st.selectbox("Housing", options=['free', 'own', 'rent'])

with col2:
    saving_accounts = st.selectbox("Saving accounts", options=['little', 'moderate', 'rich', 'quite rich'])
    checking_account = st.selectbox("Checking account", options=['little', 'moderate', 'rich'])
    credit_amount = st.number_input("Credit Amount", min_value=0, value=1000)
    duration = st.number_input("Duration", min_value=1, value=12)

# --- Mapping dictionaries ---
sex_map = {'female': 0, 'male': 1}
housing_map = {'free': 0, 'own': 1, 'rent': 2}
saving_map = {'little': 0, 'moderate': 1, 'rich': 2, 'quite rich': 3}
checking_map = {'little': 0, 'moderate': 1, 'rich': 2}

# --- Prepare input DataFrame ---
input_data = pd.DataFrame({
    'Age': [age],
    'Sex': [sex_map[sex]],
    'Job': [job],
    'Housing': [housing_map[housing]],
    'Saving accounts': [saving_map[saving_accounts]],
    'Checking account': [checking_map[checking_account]],
    'Credit amount': [credit_amount],
    'Duration': [duration]
})

# --- Predict ---
if st.button("Predict Risk"):
    prediction = model.predict(input_data)[0]
    prob_good = model.predict_proba(input_data)[0][1]  # Probability of GOOD risk
    
    st.markdown("---")
    
    if prediction == 1:
        st.success(f"✅ The applicant is predicted to be a **GOOD credit risk**")
        st.progress(int(prob_good * 100))
        st.write(f"Probability of GOOD risk: {prob_good:.2f}")
    else:
        st.error(f"❌ The applicant is predicted to be a **BAD credit risk**")
        st.progress(int((1 - prob_good) * 100))
        st.write(f"Probability of BAD risk: {1 - prob_good:.2f}")
