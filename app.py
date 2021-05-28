import streamlit as st
import requests
import datetime

'''# Simo's taxi fare prediction'''

st.markdown('''A simple API to estimate taxi fares based on route and time indications''')

'''
## Provide simobot with the details of your route 🤔 
'''
st.text("")

date = st.date_input('Please insert your date')
time = st.time_input('Please insert your date and time')
pickup_datetime = f'{date} {time}'
pickup_lon = st.text_input('Enter your pickup longitude', '40.7614327')
pickup_lat = st.text_input('Enter your pickup latitude', '-73.9798156')
dropoff_lon = st.text_input('Enter your dropoff longitude', '40.6513111')
dropoff_lat = st.text_input('Enter your dropoff latitude', '-73.8803331')
passenger_count = st.text_input('Enter the amount of passengers', '2')


# test_url = 'https://taxifare.lewagon.ai/predict?pickup_datetime=2012-10-06%2012:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2'
url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':
#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# 2. Let's build a dictionary containing the parameters for our API...

user_params = dict(
    pickup_datetime=pickup_datetime,
    pickup_longitude=pickup_lon,
    pickup_latitude=pickup_lat,
    dropoff_longitude=dropoff_lon,
    dropoff_latitude=dropoff_lat,    
    passenger_count=passenger_count
    )

# check if params assignment works
# st.write(user_params)

# 3. Let's call our API using the `requests` package...

response = requests.get(
    url,
    params=user_params
)
prediction = round(response.json()['prediction'],1)
# response = requests.get(
#     test_url
# )

'''

'''
# if response.status_code == 200:
#     st.write("API call success")
# else:
#     st.write("API call error")
# st.write(response.json())

st.text("")

if st.button('predict'):
    # print is visible in server output, not in the page
    # st.write('I was clicked 🎉')
    # st.write(prediction)
    
    st.write(f"##🎉 simoBot's prediction: {prediction} $")