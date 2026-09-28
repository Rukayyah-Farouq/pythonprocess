import requests

url = 'https://api.open-meteo.com/v1/forecast'
params = {
    'latitude':12.00,
    'longitude': 8.52,
    'current': 'temperature_2m, relative_humidity_2m, wind_speed_10m'
}
response = requests.get(url, params=params)
data = response.json()
print(data)
