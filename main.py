import os
import requests
from twilio.rest import Client

API_KEY = os.environ.get("OWM_API_KEY")
lat = 18.520430
long = 73.856743
URL = 'https://api.openweathermap.org/data/2.5/forecast?'
account_sid = 'AC500d95b76da5f244ea65ac724e9e45a1'
auth_token = os.environ.get("AUTH_TOKEN")


parameters = {
    "lat": 42.762859,
    "lon": 11.112780,
    "appid": API_KEY,
    "cnt": 4
}

# step : 1 Getting Access to weather Data by using API.
response = requests.get(url=URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

# step : 2 Getting Hold of Hourly Forecast from weather_data.
will_rain = False
for hour_data in weather_data["list"]:
    weather_id = hour_data['weather'][0]['id']
    if int(weather_id) < 700:
        will_rain = True



# step : 3 Sending SMS For Rain ALert.
# using twillio API.
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today.Remember to bring ☂️today",
        from_="+18437514501",
        to="+917840988243",
    )
    print(message.status)
