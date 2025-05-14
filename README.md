# 🏠 House Price Prediction

A machine learning web application that predicts house prices in Bengaluru based on user input like location, number of bedrooms, square footage, and more.

---

## 📂 Folder Structure
<pre> 
  📦 house-price-prediction/ 
        ├── static/ 
        │ ├── image.jpg 
        │ ├── link.png 
        │ ├── logo.jpg 
        │ ├── style.css 
        │ └── unnamed.png 
        ├── templates/ 
        │ ├── about.html 
        │ ├── contact.html 
        │ ├── index.html 
        │ └── layout.html 
        ├── Bengaluru_House_Data.csv 
        ├── Preparing_Data.ipynb 
        ├── Training_model.ipynb 
        ├── prepared_data.csv 
        ├── model.pkl 
        ├── ohe.pkl 
        ├── app.py 
        ├── description.txt 
        ├── requirements.txt 
        └── README.md </pre>


---

## 💡 Features

- Predicts house prices in Bengaluru based on user input
- Clean and simple web UI using HTML and CSS
- Trained using Linear Regression and One-Hot Encoding
- Built with Flask backend and Python ML tools

---

## 📊 Tech Stack

- Python (pandas, numpy, scikit-learn)
- Flask
- HTML & CSS
- Jupyter Notebook for data preparation & model training

---

## 📈 How It Works

1. Data cleaning and feature engineering on `Bengaluru_House_Data.csv`
2. One-hot encoding of categorical variables
3. Training a Linear Regression model on the processed dataset
4. Saving the model and encoder using `pickle`
5. Web UI takes input and displays predicted price using Flask

---

## ▶️ How to Run Locally
```bash

git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction

pip install -r requirements.txt

python app.py
```
Open browser and navigate to <br>
http://127.0.0.1:5000/

