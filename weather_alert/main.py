import requests
from twilio.rest import Client


OWN_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = "@@@@"
MY_LAT = 32.821150
MY_LONG = 34.969876
ACCOUNT_SID = '@@@'
AUTH_TOKEN = '@@@'

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 10,
}

response = requests.get(OWN_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()['list']

will_rain = False
for weather_list in weather_data:
    for weather in weather_list['weather']:
        if weather['id'] < 700:
            will_rain = True

client = Client(ACCOUNT_SID, AUTH_TOKEN)
message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+16206829024',
                     to='+97258111111'
                 )
print(message.status)

if will_rain:
    print("Bring an umbrella!")

