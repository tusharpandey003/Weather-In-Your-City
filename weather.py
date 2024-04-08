from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="new delhi"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?&appid={
        os.getenv("api_key")}&q={city}&units=metric"
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print("\n*** get weather conditions***")

    city = input("\nplease enter a city name:")
    if not bool(city.strip()):
        city = "new delhi"
    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
