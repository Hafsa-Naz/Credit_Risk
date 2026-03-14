# Credit Risk Prediction System

Credit Risk Prediction System using Python & ML to classify applicants as **Good Risk** or **Bad Risk**. Includes a **Streamlit web app** for interactive predictions.

## Dataset
- German Credit Dataset, 1000 records, 11 features  
- Target: `Risk`  
- File: `german_credit_data.csv`  

## Preprocessing
- Removed missing/duplicate data, dropped irrelevant columns  
- Label encoding of categorical features  
- Split into features (X) and target (y)  
- Encoders saved as `.pkl` for prediction

## Features
- Age, Sex, Job, Housing, Saving accounts, Checking account, Credit amount, Duration  
- Target: Risk

## Models & Performance
| Model                  | Accuracy |
|------------------------|----------|
| Decision Tree          | 0.58     |
| Random Forest          | 0.62     |
| Extra Trees Classifier | 0.67 ✅  |
| XGBoost                | 0.67     |

**Saved Model:** `best_et_model.pkl`

## Streamlit App
- Inputs: Age, Gender, Job, Housing, Saving/Checking account, Credit amount, Duration  
- Output: Good Risk / Bad Risk  
- **Live Demo:** [Click Here](https://creditrisk-ccuj9aappyqh3wpnb9bsocb.streamlit.app/)

## Tech Stack
- **Programming Languages & Libraries:** Python, Pandas, NumPy, Scikit-learn, XGBoost, Joblib, Streamlit  
- **Tools:** Jupyter Notebook, Git, GitHub  

## Future Improvements
- Feature engineering for higher accuracy  
- Explainable AI with SHAP/LIME  
- Add more financial variables  
- Enhance Streamlit UI & charts  

## Author
**Hafsa Naz**  
BS Artificial Intelligence, Dawood University of Engineering and Technology  
[LinkedIn](https://www.linkedin.com/in/hafsa-naz-) | [Live App](https://creditrisk-ccuj9aappyqh3wpnb9bsocb.streamlit.app/)
