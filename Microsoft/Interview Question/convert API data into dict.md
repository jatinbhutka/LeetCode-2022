# convert API data into dict:


Request Module: Links: https://realpython.com/python-requests/

Json Module: Link: https://www.w3schools.com/python/python_json.asp


API: https://api.covid19api.com/summary

```
{
ID: "ba58af41-773a-44ad-a55f-100f097a607a",
Message: "",
Global: {
        NewConfirmed: 1715223,
        TotalConfirmed: 453687490,
        NewDeaths: 7026,
        TotalDeaths: 6027063,
        NewRecovered: 0,
        TotalRecovered: 0,
        Date: "2022-03-12T02:36:30.781Z"
       },
Countries: [
            {
              ID: "7192f30f-b3a1-4b0a-9726-25da7b0e4464",
              Country: "Afghanistan",
              CountryCode: "AF",
              Slug: "afghanistan",
              NewConfirmed: 81,
              TotalConfirmed: 175974,
              NewDeaths: 1,
              TotalDeaths: 7640,
              NewRecovered: 0,
              TotalRecovered: 0,
              Date: "2022-03-12T02:36:30.781Z",
              Premium: { }
            },
            {
              ID: "c88a7075-ff14-4780-8775-5f2734da8982",
              Country: "Albania",
              CountryCode: "AL",
              Slug: "albania",
              NewConfirmed: 73,
              TotalConfirmed: 272552,
              NewDeaths: 1,
              TotalDeaths: 3485,
              NewRecovered: 0,
              TotalRecovered: 0,
              Date: "2022-03-12T02:36:30.781Z",
              Premium: { }
            },
            .
            .
            .
            ]
```


```python
import requests
import json

url = 'https://api.covid19api.com/summary'
response = requests.get(url)
print(response)

response = response.text
#print(response)

response_info =  json.loads(response)
#print(response_info)

res = {}
for country in response_info["Countries"]:
    countryName = country['Country']
    total_death = country['TotalDeaths']
    res[countryName] = total_death
print(res)
```


# Method 2:
```python
import requests
import json

url = 'https://api.covid19api.com/summary'
response = requests.get(url)
response = response.json()

res = []
for country in response['Countries']:
    res.append([country['Country'],country["CountryCode"] ])

print(res)
```


```python
# Get All the Earthquakes places
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'

import requests, json
response = requests.get(url).text


response_info = json.loads(response)
response_info = response_info['features']
#print(response_info['features'])

res = []
for feature in response_info:
    res.append(feature['properties']['place'])
    
print(res)
```

```python
# Get all countries and Covid Death:

```
