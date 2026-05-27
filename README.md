# Invoice Classification API

A machine learning based REST API that classifies invoice expenses such as Logistics, Travel, Utilities, Inventory, Office Supplies, and Cloud/Software.

Built using:
- Python
- Flask
- Scikit-learn
- TF-IDF
- Logistic Regression
- Streamlit

---

# Features

- REST API using Flask
- Machine Learning based classification
- TF-IDF preprocessing
- Logistic Regression model
- Confidence score prediction
- Streamlit frontend interface
- JSON request/response support

---

# Project Structure

invoice-classifier/
  - app.py
  - main.py
  - train_model.py
  - data.csv
  - model.pkl
  - vectorizer.pkl
  - accuracy.txt
  - requirements.txt
  - README.md

---

# Setup Instructions

## 1. Clone Repository
- git clone https://github.com/BhumikaSasmal/Invoice-Classifier
- cd invoice-classifier
## 2. Create Virtual Environment
python -m venv .venv
### Activate virtual environment:
####  Windows
.venv\Scripts\activate
#### Mac/Linux
source .venv/bin/activate

---

## 3. Install Dependencies

pip install -r requirements.txt


---

## 4. Train Model


python train_model.py


This generates:
- model.pkl
- vectorizer.pkl
- accuracy.txt

---

## 5. Run Flask API

python main.py

- A local link will be generated where the API runs. Requests to the API can be made with tools like Postman.

---

## 6. Run Streamlit Frontend

Open another terminal while the Flask app is running:

streamlit run app.py

- A link will be generated where the frontend runs. Follow the link to experience the frontend.
---

# API Usage Examples

## POST /predict
### Request Body

{
    "text": "Blue Dart courier charges for warehouse delivery"
}


### Sample Response

{
    "category": "Logistics",
    "confidence": 49.28,
    "model_accuracy": "83.33%"
}

<img width="1959" height="946" alt="image" src="https://github.com/user-attachments/assets/36ae0a76-1c1d-47b9-ae26-5750ef08638a" />


---


# Accuracy

Current model accuracy: 83.33%
