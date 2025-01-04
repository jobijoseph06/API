import requests
from send_email import send_email

api_key = "bc07434d1e9a420cb0983d8f5ac3b60a"

url = "https://newsapi.org/v2/everything?q=tesla&from=2024-12-04&sortBy=publishedAt&apiKey=bc07434d1e9a420cb0983d8f5ac3b60a"

request = requests.get(url)
content = request.json()
print(content)

body = ""

for article in content["articles"]:
   body = body + str(article["title"]) + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message = body)

