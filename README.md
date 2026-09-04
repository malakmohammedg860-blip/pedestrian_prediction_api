Pedestrian Prediction API 🚶‍♂️📊



A Machine Learning API for predicting pedestrian counts using time-series features and an optimized XGBoost model.



&#x20;Project Overview



This project is part of a Smart Piezoelectric Tile solution designed to predict pedestrian movement and support energy-generation applications.



The API receives 10 engineered features and returns the predicted number of pedestrians.



&#x20;Machine Learning

Model: Optimized XGBoost

Evaluation: TimeSeriesSplit

R² Score: Approximately 0.88

Target: Pedestrian count (Total\_Aston)

Features



The model uses:



Hour

Day of Week

Month

Is Weekend

Lag 1

Lag 2

Lag 3

Lag 6

Lag 12

Lag 24

🛠️ Technologies

Python

FastAPI

XGBoost

Scikit-learn

Pandas

NumPy

Joblib

 API Endpoint

POST /predict



Example request:



{

&#x20; "f1": 10,

&#x20; "f2": 2,

&#x20; "f3": 9,

&#x20; "f4": 1,

&#x20; "f5": 15,

&#x20; "f6": 20,

&#x20; "f7": 18,

&#x20; "f8": 25,

&#x20; "f9": 30,

&#x20; "f10": 35

}



Example response:



{

&#x20; "input": \[10, 2, 9, 1, 15, 20, 18, 25, 30, 35],

&#x20; "prediction": 4176.375

}

&#x20;My Role



As part of the AI Team, I worked on:



Data preprocessing

Feature engineering

Time-series pedestrian prediction

Machine learning model development

Model evaluation

FastAPI development and API integration

&#x20;Project Support



The project received support from the Information Technology Industry Development Agency (ITIDA), which helped motivate the team to further develop the idea and strengthen its technical implementation.

