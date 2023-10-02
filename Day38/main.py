


# exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# sheet_endpoint = "https://api.sheety.co/6d60f137ed407e317c9226df8245cc72/dailyWorkTracker/sheet1"




import requests
from datetime import datetime

today = datetime.now()
date = today.strftime("%d/%m/%y")
time = today.strftime("%X")

GENDER = "Male"
WEIGHT_KG = "69"
HEIGHT_CM = "175"
AGE = "21"

APP_ID = "38d9b6f2"
API_KEY = "225be3f7b456571dabb092a40eda26a9"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")
headers = {
"x-app-id": APP_ID,
"x-app-key": API_KEY,
}
parameter = {
"query": 'exercise_test',
"gender": GENDER,
"weight_kg": WEIGHT_KG,
"height_cm": HEIGHT_CM,
"age": AGE
}
response = requests.post(url=exercise_endpoint, json=parameter, headers=headers)
result = response.json()
print(result)
sheety_api = "https://api.sheety.co/6d60f137ed407e317c9226df8245cc72/dailyWorkTracker/sheet1"
for exercise in result["exercises"]:
    sheet_input = {
    "sheet1": {
    "date": "date",
    "time": "time",
    "exercise": exercise['name'],
    "duration": exercise['duration_min'],
    "calories": exercise['nf_calories']
    }
    }
    sheet_response = requests.post(url=sheety_api, json=sheet_input, headers=headers)
    print(sheet_response.text)    