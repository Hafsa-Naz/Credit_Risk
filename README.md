# Credit Risk Prediction System

## Project Overview

This project is a **Credit Risk Prediction System** built using **Python**.
It predicts whether a credit applicant is **“good” or “bad”** based on their personal and financial information.

The system applies multiple **machine learning algorithms** and selects the best-performing model to classify the credit risk of applicants.

---

## Dataset

The project uses the **German Credit Data** dataset which contains information about applicants and their credit details.

### File Used

* `german_credit_data.csv` – contains applicant information and credit risk labels.

### Dataset Size

* **Records:** 1000
* **Columns:** 11

### Features

| Feature          | Description                      |
| ---------------- | -------------------------------- |
| Age              | Age of the applicant             |
| Sex              | Gender of the applicant          |
| Job              | Job category                     |
| Housing          | Housing status (own, rent, free) |
| Saving accounts  | Savings account status           |
| Checking account | Checking account status          |
| Credit amount    | Credit amount requested          |
| Duration         | Duration of credit in months     |
| Purpose          | Purpose of the credit            |
| Risk             | Credit risk (good / bad)         |

---

## Data Cleaning & Preprocessing

Before building the machine learning models, the dataset was cleaned and prepared.

### Steps Performed

* Removed missing values
* Checked for duplicate records
* Dropped unnecessary column (`Unnamed: 0`)
* Encoded categorical variables using **LabelEncoder**
* Split dataset into **features (X)** and **target (y)**

Encoded features include:

* Sex
* Housing
* Saving accounts
* Checking account
* Risk (target variable)

---

## Exploratory Data Analysis (EDA)

Exploratory analysis was performed to understand the dataset.

### Analysis Performed

* Histogram distribution of **Age, Credit Amount, and Duration**
* Boxplots to identify **outliers**
* Count plots for **categorical features**
* Correlation heatmap for numeric variables
* Analysis of **Credit Amount by Job and Gender**
* Risk comparison with numeric variables

---

## Feature Selection

Selected features used for training the model:

```
Age
Sex
Job
Housing
Saving accounts
Checking account
Credit amount
Duration
```

**Target Variable**

```
Risk
```

---

## Model Training & Evaluation

Multiple machine learning models were trained and tuned using **GridSearchCV**.

| Model                  | Accuracy |
| ---------------------- | -------- |
| Decision Tree          | 0.58     |
| Random Forest          | 0.62     |
| Extra Trees Classifier | 0.67     |
| XGBoost Classifier     | 0.67     |

**Best Model:** Extra Trees Classifier

The trained model was saved as:

```
best_et_model.pkl
```

---

## Technologies Used

### Programming Language

Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Joblib

### Tools

* Jupyter Notebook
* Git
* GitHub

---

## Future Improvements

* Build a **web application using Streamlit**
* Add more financial features to improve prediction
* Use **feature engineering** to enhance model performance
* Implement **model explainability techniques (SHAP / LIME)**

---

## Author

**Hafsa Naz**
BS Artificial Intelligence Student
Dawood University of Engineering & Technology

🔗 LinkedIn
https://www.linkedin.com/in/hafsa-naz-
