# import requests

# city_name='Sambhal'
# API_key='9053b91e3917f0a81c942cdb48dd9854'
# url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
# response = requests.get(url)
# if response.status_code==200:
#     print('OK')
#     data = response.json()
#     #print(data)
#     #print(data['weather'])
#     #print(data['weather'][0])
#     print(f"Temperature : {data['main']['temp']} C")
#     print("---------")
#     print("Condition "+" :"+data['weather'][0]['description'])
#     print("---------")
#     print(f"Humidity : {data['main']['humidity']}%")
#     print("---------")
#     print(f"Wind Speed {data['wind']['speed']} m/s")
#     print("---------")
# else:
#     print('fail')

print(u'5\N{DEGREE SIGN}')
