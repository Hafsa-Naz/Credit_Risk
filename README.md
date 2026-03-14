# Credit Risk Prediction System

## Project Overview
This project is a **Credit Risk Prediction System** built using **Python and Machine Learning**.  
The goal of this project is to predict whether a credit applicant is a **Good Risk** or **Bad Risk** based on their financial and personal information.

Several machine learning models were trained and compared, and the best-performing model was selected for prediction. A **Streamlit web application** was also developed to allow users to interact with the model and make predictions easily.

---

## Dataset
The project uses the **German Credit Dataset**, which contains information about loan applicants.

**File Used**
- german_credit_data.csv

**Dataset Size**
- Records: 1000  
- Features: 11  

**Features in Dataset**
- Age
- Sex
- Job
- Housing
- Saving accounts
- Checking account
- Credit amount
- Duration
- Purpose
- Risk (target variable)

---

## Data Cleaning and Preprocessing
Before training the models, the dataset was cleaned and prepared.

Steps performed:
- Removed missing values
- Checked and removed duplicate records
- Dropped unnecessary column (`Unnamed: 0`)
- Encoded categorical features using **LabelEncoder**
- Split the dataset into **features (X)** and **target variable (y)**

Encoded variables include:
- Sex
- Housing
- Saving accounts
- Checking account
- Risk

The trained encoders were saved as `.pkl` files for later use in prediction.

---

## Exploratory Data Analysis (EDA)
Exploratory data analysis was performed to better understand the dataset.

Key analysis performed:
- Distribution plots for **Age, Credit Amount, and Duration**
- Boxplots for detecting outliers
- Count plots for categorical variables
- Correlation heatmap for numeric features
- Comparison of credit amount by **job and gender**
- Risk comparison with numeric variables

---

## Feature Selection
The following features were used for model training:

Age  
Sex  
Job  
Housing  
Saving accounts  
Checking account  
Credit amount  
Duration  

**Target Variable:** Risk

---

## Model Training and Evaluation
Multiple machine learning models were trained and tuned using **GridSearchCV**.

Models tested:
- Decision Tree
- Random Forest
- Extra Trees Classifier
- XGBoost

Model performance:

Decision Tree Accuracy: 0.58  
Random Forest Accuracy: 0.62  
Extra Trees Accuracy: 0.67  
XGBoost Accuracy: 0.67  

The **Extra Trees Classifier** was selected as the final model.

Saved model file:
- best_et_model.pkl

---

## Streamlit Web Application
A **Streamlit application** was developed to make the model interactive.

Users can enter the following information:
- Age
- Gender
- Job category
- Housing status
- Saving account status
- Checking account status
- Credit amount
- Loan duration

The application predicts whether the applicant is a **Good Risk** or **Bad Risk**.

---

## Running the Streamlit App

Install required libraries:

pip install streamlit pandas numpy scikit-learn xgboost joblib

Run the application:

streamlit run app.py

The application will open automatically in your browser.

---

## Technologies Used

Programming Language:
- Python

Libraries:
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Joblib
- Streamlit

Tools:
- Jupyter Notebook
- Git
- GitHub
- Streamlit

---

## Future Improvements
- Improve model performance using feature engineering
- Add explainable AI methods (SHAP or LIME)
- Deploy the Streamlit application online
- Add more financial attributes for better predictions

---

## Author
Hafsa Naz  
BS Artificial Intelligence Student  
Dawood University of Engineering and Technology  

LinkedIn:  
https://www.linkedin.com/in/hafsa-naz-
