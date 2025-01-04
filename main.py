import requests
from send_email import send_email

api_key = "bc07434d1e9a420cb0983d8f5ac3b60a"
topic = "tesla"

url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&from=2024-12-04&"
       "sortBy=publishedAt&"
       "apiKey=bc07434d1e9a420cb0983d8f5ac3b60a&""language=en")

request = requests.get(url)
content = request.json()
print(content)

body = ""

for article in content["articles"][0:20]:
   body = ("Subject: Today's news" +"\n" +
           body + str(article["title"]) + "\n" +
           str(article["description"]) + "\n" +
           article["url"]+ 2*"\n")

body = body.encode("utf-8")
send_email(message = body)

