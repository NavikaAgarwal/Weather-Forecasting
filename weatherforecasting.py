from gtts import gTTS
import os
import requests
import json

def get_weather_data(city):
    api_key = "086e02960a374c7892c73933240306"  # Replace with your valid API key
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print(f"Error fetching data: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error with the request: {e}")
        return None

def announce_weather(city, weather_data):
    if weather_data:
        region = weather_data["location"]["region"]
        temperature = weather_data["current"]["temp_c"]

        # Create TTS object and save the audio file
        tts = gTTS(f"The region of {city} is {region}. The temperature is {temperature} degrees Celsius.")
        tts.save("weather.mp3")

        # Play the audio file
        os.system("start weather.mp3")

        # Print to console
        print(f"Region: {region}")
        print(f"Temperature: {temperature}°C")
    else:
        print("Could not retrieve weather data.")

def main():
    print("Welcome to the Weather Forecasting Application.")
    city = input("Enter your city: ")
    weather_data = get_weather_data(city)
    announce_weather(city, weather_data)
    print("Thanks for using the Weather Forecasting Application.")

if __name__ == "__main__":
    main()