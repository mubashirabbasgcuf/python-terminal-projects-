import requests
import json
print("business, entertainment ,general ,health ,science,sports ,technology ,")
query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=841c340ed70b430cbb38f1383e8c0712"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("--------------------------------------")
  
