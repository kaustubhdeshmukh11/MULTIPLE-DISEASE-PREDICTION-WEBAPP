# Multiple Disease Prediction Web App

A Django-based web application that predicts the likelihood of multiple diseases—including heart disease, diabetes, Parkinson’s disease, and breast cancer—using machine learning models. The project integrates logistic regression, SVM, and neural networks to deliver robust, real-time predictions. Detailed exploratory data analysis (EDA) was conducted on healthcare datasets to extract key features for accurate predictions.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data & Model Details](#data--model-details)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Future Improvements](#future-improvements)
- [License](#license)
- [Contact](#contact)

## Overview
This project leverages the Django web framework to build an intuitive interface where users can input their health parameters. The application then uses pre-trained machine learning models to predict the probability of the presence of:
- **Heart Disease**
- **Diabetes**
- **Parkinson’s Disease**
- **Breast Cancer**

EDA was performed on relevant healthcare datasets to identify and extract the most influential features. The models were then trained using these features to ensure high prediction accuracy.

## Features
- **Multi-Disease Prediction:** Simultaneously predicts four diseases.
- **Integrated ML Models:** Combines logistic regression, SVM, and neural networks for robust predictions.
- **Real-Time Inference:** Provides fast and accurate predictions through a web interface.
- **Data-Driven Insights:** Uses key features extracted from thorough EDA.
- **User-Friendly Interface:** Developed with Django for ease of use.

## Architecture
- **Backend:** Django handles the web routing, data processing, and integrates the ML models.
- **Machine Learning:** Models developed using scikit-learn and deep learning libraries (e.g., TensorFlow/Keras).
- **Frontend:** HTML/CSS templates rendered via Django for user interaction.
- **Data:** Public healthcare datasets are preprocessed and used for training the models.

## Technologies Used
- **Languages:** Python, HTML, CSS
- **Frameworks:** Django
- **Machine Learning Libraries:** scikit-learn, TensorFlow/Keras
- **Data Analysis:** Pandas, NumPy, Matplotlib/Seaborn (for EDA)
- **Version Control:** Git, GitHub

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/multiple-disease-prediction-webapp.git
    cd multiple-disease-prediction-webapp
    ```
2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```
5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```
6. **Access the application:**
   Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

1. **Home Page:**  
   The landing page contains a form where users can enter health parameters.
2. **Data Input:**  
   Users provide necessary details (e.g., age, blood pressure, cholesterol levels).
3. **Prediction Process:**  
   On submission, the backend processes the input using integrated ML models.
4. **Results:**  
   The predictions are displayed on a results page, showing the probability for each disease.

## Data & Model Details

- **Data:**
  - Publicly available healthcare datasets.
  - Extensive EDA was performed to identify key predictive features (e.g., age, blood pressure, cholesterol, etc.).
- **Models:**
  - **Logistic Regression:** For binary classification tasks.
  - **Support Vector Machine (SVM):** For robust classification.
  - **Neural Network:** To capture complex non-linear relationships.
- **Training:**  
  The models were trained using the preprocessed datasets. Techniques like hyperparameter tuning and cross-validation were used to optimize performance.

## Project Structure

