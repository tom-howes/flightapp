import requests

url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchAirport"

querystring = {"query":"london","locale":"en-US"}

headers = {
	"x-rapidapi-key": "397f33e22bmsh01328fc3eb3099cp1fc14ejsnca5184158bdb",
	"x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

airports = response.json()['data']

for i in range(len(airports)):
    print(airports[i]['presentation']['suggestionTitle'])
    print(airports[i]['skyId'])
