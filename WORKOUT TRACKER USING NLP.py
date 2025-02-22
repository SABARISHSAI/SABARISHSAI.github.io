import requests
from datetime import datetime

APP_ID = "3578525e"
APP_KEY = "e3bf1f07844f2ffd904c5168ad32208a"
NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
path = #your own
SHEETY_ENDPOINT = f"https://api.sheety.co/{path}/workouttrack/sheet1"

now = datetime.now()
current_date = now.strftime("%d/%m/%y")
current_time = now.strftime("%H:%M:%S")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}

query = input("What did you do today? ")

data = {"query": query}
response = requests.post(NUTRITIONIX_URL, headers=headers, json=data)

if response.status_code == 200:
    exercises = response.json().get("exercises", [])

    if not exercises:
        print("⚠️ No exercise data found! Please check your input.")
    else:
        for exercise in exercises:
            duration = round(exercise["duration_min"], 2)  
            calories = round(exercise["nf_calories"], 2)  

            workout_data = {
                "sheet1": {
                    "date": current_date,
                    "time": current_time,
                    "exercise": exercise["name"].title(),  
                    "duration": f"{duration} min",  
                    "calories": calories
                }
            }

            print("🔹 Sending data:", workout_data)  

            sheet_response = requests.post(SHEETY_ENDPOINT, json=workout_data)

            if sheet_response.status_code == 200:
                print("✅ Successfully added to sheet:", sheet_response.json())
            else:
                print(f"❌ Error {sheet_response.status_code}: {sheet_response.text}")

else:
    print(f"❌ Error {response.status_code}: {response.text}")
