import datetime
import requests
response = requests.get("https://github.com/avielffflaksdmlajsndajlsd")
if response.status_code == 200:
    print("github is up and running")
else:
    print("github is down " + str(response.status_code))

print(datetime.datetime.now())
