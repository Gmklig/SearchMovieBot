import http.client

conn = http.client.HTTPSConnection("http://api.kinopoisk.cf")

payload = "{}"

conn.request("GET", "/getFilm?filmID=714888", payload)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))