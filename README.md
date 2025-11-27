Project Overview

This project focuses on predicting water potability using machine learning. The goal is to assess water safety based on various quality indicators, such as pH, hardness, and chemical concentrations.

The dataset is analyzed to handle missing values, explore feature relationships, and address potential imbalances, aiming to create a robust predictive model. The project emphasizes proactive water quality management and contributes to efforts for global access to clean and safe drinking water.

Exploratory Data Analysis (EDA)

EDA includes:

Visualizing missing values

Understanding the distribution of potability

Exploring relationships between features

Calculating correlations

Creating histograms for feature distributions

These steps provide a comprehensive understanding of the dataset before modeling.

Machine Learning Models and Results

I applied several machine learning classifiers to predict water potability:

Logistic Regression

Decision Tree Classifier

Random Forest Classifier

K-Nearest Neighbors (KNN)

Support Vector Classifier (SVM)

Naive Bayes

XGBoost

Among these, SVM performed the best, demonstrating high accuracy and a balanced precision-recall trade-off.

Application Deployment

I developed a Flask web application for user-friendly interaction. Users can input water quality parameters into a web form and receive real-time predictions. The application code is hosted on GitHub
.

How to Run the Flask Application

Clone the Repository:

git clone https://github.com/YourUsername/Water-Quality-Prediction.git


Navigate to the Project Directory:

cd Water-Quality-Prediction


Install Dependencies:

pip install -r requirements.txt


Run the Flask App:

python app.py


This will start the Flask development server.

Access the Application:

Open your browser and go to http://127.0.0.1:5000/
. You will see the water quality prediction form.

Input Water Quality Parameters:

Provide values for:
pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, turbidity.

Submit the Form:

Click the “Predict Potability” button to view the results.

Explore Results:

The app will display the predicted water quality: Potable (Safe) or Not Potable (Unsafe).
