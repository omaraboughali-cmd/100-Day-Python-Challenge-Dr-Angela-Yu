import requests

import datetime

import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

today = datetime.datetime.now()

# today = today.strftime()

APP_ID = 'app_a01d20df46de4d38a704335d'

API_KEY = 'nix_live_TI5Heiq6O7hz01m4e1rcG7U86wCixQnc'

BASE_URL = 'https://app.100daysofpython.dev'

SHEETY_API = 'https://api.sheety.co/8bd626147e5c625d6dc93203a45aa408/workoutTracking/sheet1'

authentication = {

    'x-app-id': APP_ID , 

    'x-app-key': API_KEY ,

}

query = {

    'query' : input('How much did you workout ')

}



response = requests.post(url=f'{BASE_URL}/v1/nutrition/natural/exercise' , headers=authentication , json=query)

data = response.json()

exercise = data["exercises"][0]

name = exercise['name']             # 'running'

duration = exercise['duration_min'] # 30

calories = exercise['nf_calories']  # 360

met = exercise['met']

today_date = today.strftime("%Y-%m-%d")  

today_time = today.strftime("%H:%M:%S")  

headers = {
    'Authorization': f'Bearer {TOKEN}' ,
    'Content-Type': 'application/json' ,

}

body = {

    'sheet1': {

        'date': today_date,

        'time': today_time,

        'exercise': exercise['name'].title(),

        'duration': exercise['duration_min'],

        'calories': exercise['nf_calories'],

    }
}

response = requests.post(SHEETY_API, json = body, headers = headers)

print(response.status_code)

print(response.json())