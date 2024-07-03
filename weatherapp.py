import requests
def main():
    api_key='9053b91e3917f0a81c942cdb48dd9854'
    while(True):
        print("Weather Report Application")
        print("1. Get Weather Information")
        print("2. Exit")
        inp = int(input("Enter Your Choice : "))
        if(inp==1):
            city=input("Enter City Name : ")
            get_weather(city,api_key)
        elif(inp==2):
            print('Exiting Application')
            break;
        else:
            print("Choose Correct Option")


def get_weather(city_name,api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response=requests.get(url)
    if response.status_code==200:
        print("ok")
        data=response.json()
        info={
            "temperature":data['main']['temp'],
            "condition":data['weather'][0]['description'],
            "humidity":data['main']['humidity'],
            "windspeed":data['wind']['speed']
        }
        display_weather(city_name,info)
    else:
        print("Fail")

def display_weather(city_name,weather_data):
    print(f"Weather in {city_name.capitalize()} : ")
    #2print(weather_data)
    
    print(f"Temperature : {weather_data['temperature']}")  
    print(f"Condition : {weather_data['condition']}")
    print(f"Humidity : {weather_data['humidity']}%")
    print(f"Wind Speed : {weather_data['windspeed']} m/s")
    print("---------------------------------------------------------\n")

main()