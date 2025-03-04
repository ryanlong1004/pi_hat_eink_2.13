import http.client

conn = http.client.HTTPSConnection("fear-and-greed-index.p.rapidapi.com")

headers = {
    "x-rapidapi-key": "WQLmJSQsxImsho6Phz1NE21seLq6p1trIPMjsnwN1hLaUUMRX5",
    "x-rapidapi-host": "fear-and-greed-index.p.rapidapi.com",
}

conn.request("GET", "/v1/fgi", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
