import http.client

conn = http.client.HTTPSConnection("sky-scrapper.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "397f33e22bmsh01328fc3eb3099cp1fc14ejsnca5184158bdb",
    'x-rapidapi-host': "sky-scrapper.p.rapidapi.com"
}

conn.request("GET", f"/api/v2/flights/searchFlights?originSkyId=LOND&destinationSkyId=NYCA&originEntityId=27544008&destinationEntityId=27537542&date=2025-05-14&cabinClass=economy&adults=1&sortBy=best&currency=USD&market=en-US&countryCode=US", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))