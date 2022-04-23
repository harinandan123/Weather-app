import requests
from datetime import datetime

user_api = "06c921750b9a82d8f5d1294e1586276f"
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
humdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
feel = ((api_data['main']['feels_like']) - 273.15)


print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print("Current temperature is: {:.2f}*C".format(temp_city))
print("Current weather desc  :",weather_desc)
print("Current Humidity      :",humdt, '%')
print("Current wind speed    :",wind_spd ,'kmph')
print("Feels like temperature :{:.2f}*C".format(feel))
