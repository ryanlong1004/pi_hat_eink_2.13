import requests

url = "https://fear-and-greed-index.p.rapidapi.com/v1/fgi"
headers = {
    "x-rapidapi-key": "WQLmJSQsxImsho6Phz1NE21seLq6p1trIPMjsnwN1hLaUUMRX5",
    "x-rapidapi-host": "fear-and-greed-index.p.rapidapi.com",
}

response = requests.get(url, headers=headers)
data = response.json()

print(data)
