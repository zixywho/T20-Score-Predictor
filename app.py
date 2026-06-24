import streamlit as st
import pickle
import numpy as np
import pandas as pd

pipe = pickle.load(open('pipe.pkl', 'rb'))
teams = ['West Indies', 'South Africa', 'New Zealand', 'India', 'Pakistan',
       'Australia', 'Bangladesh', 'Sri Lanka', 'England']
cities = ['Chester-le-Street', 'Kanpur', 'Nagpur', 'Bangalore', 'Lauderhill',
       'Dubai', 'Abu Dhabi', 'Sydney', 'Hobart', 'Melbourne',
       'Wellington', 'Auckland', 'Hamilton', 'Bloemfontein',
       'Potchefstroom', 'Barbados', 'Trinidad', 'Colombo', 'Jamaica',
       'Nelson', 'Mount Maunganui', 'Ranchi', 'Guwahati', 'Birmingham',
       'Manchester', 'Cardiff', 'Bristol', 'Delhi', 'Rajkot',
       'Thiruvananthapuram', 'Lahore', 'Johannesburg', 'Centurion',
       'Cape Town', 'Cuttack', 'Indore', 'Mumbai', 'Dhaka', 'Sylhet',
       'Karachi', 'Harare', 'Carrara', 'Brisbane', 'St Kitts', 'Kolkata',
       'Lucknow', 'Chennai', 'Gros Islet', 'Basseterre', 'Visakhapatnam',
       'Bengaluru', 'Adelaide', 'Canberra', 'Perth', 'East London',
       'Durban', 'Port Elizabeth', 'Chandigarh', 'Hyderabad',
       'Christchurch', 'Napier', 'Providence', 'Kandy', 'Southampton',
       'Pune', 'Dunedin', 'Paarl', 'Nottingham', 'Leeds', 'Ahmedabad',
       'Coolidge', 'Bridgetown', "St George's", 'Sharjah', 'Jaipur',
       'Dharamsala', 'Roseau', 'Tarouba', 'Kingston', 'Queenstown',
       'Rawalpindi', 'Chattogram', 'London', 'Gqeberha', 'Raipur',
       'Hangzhou', 'New York', 'Dallas', 'North Sound', 'Kingstown',
       'Gwalior', 'Dambulla', 'Darwin', 'Cairns', 'New Chandigarh',
       'Nairobi', 'King City', 'Guyana', 'St Lucia', 'Antigua',
       'Pallekele', 'Mirpur', 'Hambantota', 'St Vincent', 'Chittagong',
       'Dominica', 'Dharmasala']

st.title('Cricket Score Predictor')
col1 , col2 = st.columns(2)

with col1:
    batting_team =  st.selectbox('Select batting team',sorted(teams))

with col2:
    bowling_team = st.selectbox('Select bowling team', sorted(teams))

city = st.selectbox('Select city', sorted(cities))

col3, col4 , col5 = st.columns(3)

with col3:
    current_score = st.number_input('Current Score')

with col4:
    overs = st.number_input('Overs Done (works for over > 5)')
with col5:
    wickets = st.number_input('Wickets out')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('Predict Score'):
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = (current_score / overs)

    input_df = pd.DataFrame(
        {'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': [city],'current_score': [current_score],
         'balls_left' : [balls_left],'wickets_left' : [wickets_left],'crr': [crr],'last_five': [last_five]}
    )

    result = pipe.predict(input_df)
    st.header("Predicted Score - " + str(int(result[0])))
