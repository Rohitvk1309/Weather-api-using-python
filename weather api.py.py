import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    params = {
        "q": city,
        "appid":  "636260b45a6741241a4ec13b5b10e7c3",
        "units": "metric"  # You can use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            # Extract relevant weather information
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]

            print(f"Weather in {city}: {weather_description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_api_key' with the actual API key you obtained from OpenWeatherMap
api_key = 'your_api_key'
city_name = input("Enter city name: ")

get_weather(api_key, city_name)
