import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
APP_ID = os.getenv("app_id")
SHEETY_KEY = os.getenv("SHEETY_KEY")

exercise = input("wpisz co robiłeś")
exercise_params = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 90,
    "height_cm": 184,
    "age": 23
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
response_nutrition = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
response_text = response_nutrition.json()

now = datetime.now()
now_date = now.strftime("%d/%m/%Y")
now_time = str(now.strftime("%X"))
print(now_date, now_time)

sheety_endpoint = "https://api.sheety.co/023c1343faf9460ce2a05f29e0e609ea/myWorkouts/workouts"
sheety_params = {
    "workout": {
        "date": now_date,
        "time": now_time,
        "exercise": response_text["exercises"][0]["name"],
        "duration": response_text["exercises"][0]["duration_min"],
        "calories": response_text["exercises"][0]["nf_calories"],
    }
}

headers_sheety = {"Authorization": f"Bearer {SHEETY_KEY}"}
response_sheety = requests.post(url=sheety_endpoint, json=sheety_params, headers=headers_sheety)

