#  Cricket Score Predictor

A Machine Learning web application that predicts the final first-innings score in a T20 cricket match based on the current match situation.

## Features

* Predicts first-innings T20 scores in real time.
* Uses match context such as:

  * Batting Team
  * Bowling Team
  * Venue/City
  * Current Score
  * Overs Completed
  * Wickets Lost
  * Runs Scored in the Last 5 Overs
* Interactive web interface built with Streamlit.
* Trained using historical international T20 match data.

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Streamlit

## Model Features

The model uses the following features:

* Batting Team
* Bowling Team
* City
* Current Score
* Balls Left
* Wickets Left
* Current Run Rate (CRR)
* Runs Scored in Last 5 Overs

## Project Structure

Cricket-Score-Predictor/

├── app.py

├── pipe.pkl

├── requirements.txt

├── README.md

└── notebooks/

```
└── model_building.ipynb
```

## Run Locally

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

## Future Improvements

* Add second innings win probability prediction.
* Include player-level statistics.
* Improve feature engineering.
* Deploy with custom styling and visualizations.

## Author

Built as a Machine Learning project using Python, XGBoost, and Streamlit.
