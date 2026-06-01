# 🏠 House Price Prediction System

Machine Learning project to predict house prices based on property features such as bedrooms, bathrooms, living area, condition, and nearby schools.

Includes a Streamlit web application for real-time house price prediction.

---

## 🚀 Features

- House Price Prediction
- Real-time Streamlit App
- Multiple Regression Models Comparison
- Hyperparameter Tuning with GridSearchCV
- Model Serialization using Joblib

---

## 📁 Dataset

Dataset: House Price India.csv

### Features
- Number of Bedrooms
- Number of Bathrooms
- Living Area
- Condition
- Number of Schools Nearby

### Target
- House Price

---

## 🤖 Models Used

| Model | MAE | MSE |
|---------|---------|---------|
| Linear Regression | 165,051.87 | 59,251,188,714.51 |
| Decision Tree Regressor | 163,053.89 | 62,811,518,790.21 |
| Random Forest Regressor | **159,392.57** | **57,887,313,460.46** |

✅ Best Model: Random Forest Regressor

---

## ⚙️ Best Parameters

### Random Forest Regressor
- max_depth = 5
- n_estimators = 10

### Decision Tree Regressor
- criterion = friedman_mse
- max_depth = 10
- min_samples_leaf = 4
- min_samples_split = 5
- splitter = random

---

## 📊 Model Performance

- Best Model: Random Forest Regressor
- MAE: 159,392.57
- MSE: 57,887,313,460.46

---

## 💻 Streamlit App

Users can:
- Enter house details
- Predict house price instantly
- View estimated property value

---

## ▶️ Run Project

pip install -r requirements.txt

streamlit run app.py

---

## 📦 Files

- app.py
- model.pkl
- House Price India.csv
- model.ipynb

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## 👨‍💻 Author

Ram Vilas
