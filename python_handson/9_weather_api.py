import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()

city = input("Enter city name: ")
weather_data = get_weather(city)
print("Weather in", city, ":")
print("Temperature:", weather_data["main"]["temp"])
print("Description:", weather_data["weather"][0]["description"])