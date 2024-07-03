import requests

def main():
    api_key = '9053b91e3917f0a81c942cdb48dd9854'
    while True:
        print("Weather Report Application")
        print("1. Get Weather Information")
        print("2. Exit")
        try:
            inp = int(input("Enter Your Choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if inp == 1:
            city = input("Enter City Name: ")
            get_weather(city, api_key)
        elif inp == 2:
            print('Exiting Application')
            break
        else:
            print("Choose Correct Option")

def get_weather(city_name, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        info = {
            "temperature": data['main']['temp'],
            "condition": data['weather'][0]['description'],
            "humidity": data['main']['humidity'],
            "windspeed": data['wind']['speed']
        }
        display_weather(city_name, info)
    except Exception as err:
        print(f"Error Occurred check city or internet connection")

def display_weather(city_name, weather_data):
    print(f"Weather in {city_name.capitalize()}:")
    print(f"Temperature: {weather_data['temperature']} °C")
    print(f"Condition: {weather_data['condition']}")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Wind Speed: {weather_data['windspeed']} m/s")
    print("---------------------------------------------------------\n")

if __name__ == "__main__":
    main()
