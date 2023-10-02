import requests
from twilio.rest import Client

params = {
    "lat" : 11.016844,
    "lon" : 76.955833,
    "appid" : 'ec9f34f8ae458c10cda319a6e04563ea'
}

account_sid = 'ACde652469f64d4ff082f680a6baccc9db'
auth_token = '24c0232853108d2fae2fcd1532a20f70'

# response = requests.get("https://api.openweathermap.org/data/3.0/onecall",params=params)
# response.raise_for_status()
# weather_data = response.json()
# weather_slice = weather_data["hourly"][:12]

will_rain = False

# while not will_rain:
#     for hour_data in weather_slice:
#         condition_code = hour_data["weather"][0]["id"] 
#         if int(condition_code) < 700:
#             will_rain = True
will_rain = True

if will_rain:
    print("Bring an umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+13343848564',
        body="Hi, Hariharan J. It's going to rain today. Remember to bring an umbrella.",
        to='+919994023452'
    )
    print(message.status)    