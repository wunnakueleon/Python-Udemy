from twilio.rest import Client
import time
import requests
import datetime
from dotmap import DotMap


api_key = ""
latitude = 16.8409
longitude = 96.1735

account_sid = ""
auth_token = ""
ph_num = ""
my_num = ""


data = requests.get(url=f"http://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}")
# print(data.raise_for_status())
data_json = DotMap(data.json())
# print(data.json())

hour_gaps = [3, 6, 9, 10, 15, 18, 21, 24]
day = 0
end_of_day = 0
old_end_of_day = 0
weather_condition = ""
 
while True:
    current_hour = datetime.datetime.now().hour
    if (current_hour in hour_gaps) :
        end_of_day = hour_gaps.index(current_hour) % len(hour_gaps) # because it starts from 0, it's not the exact length

        if (end_of_day != old_end_of_day):
            weather_condition = data_json.list[end_of_day].weather[0].description
            print(weather_condition)
            client = Client(account_sid, auth_token)
            message = client.messages .create (
                        body=f"{weather_condition}: Do as you see fit!🤩",
                        from_=ph_num,
                        to=my_num
                    )
            print(message.body)
            if (end_of_day == len(hour_gaps) - 1):
                day += 1

            if (day == 5):
                data = requests.get(url="http://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}")
                data_json = data.json()
                day = 0
                
            old_end_of_day = end_of_day

    time.sleep(60)
        


    







