
import requests

API_KEY = "YOUR_API_KEY"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        print("\n===== WEATHER REPORT =====")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"])
    else:
        print("City not found or API error.")

except requests.exceptions.RequestException:
    print("Please check your internet connection.")
