import requests
from datetime import datetime
#from requests.auth import HTTPBasicAuth

API_KEY = "apikey"
APP_ID = "app_id"

sheet_endpoint = "https://api.sheety.co/309683bd59446b9497bad9f8cf4b8bba/copyOfMyWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

post_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise,
    "gender": "male",
    "age": "20",
    "weight_kg": "64",
    "height_cm": "164"
}

today = datetime.now()
date = today.strftime("%Y/%m/%d")
now_time = datetime.now().strftime("%X")

response = requests.post(url=post_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

for exercise in result["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": date,
            "time": now_time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    } 

    auth_header = {
        "Authorization": "auth_header"
    }

    response = requests.post(sheet_endpoint, json=sheety_parameters, headers=auth_header)
    print(response.text)



