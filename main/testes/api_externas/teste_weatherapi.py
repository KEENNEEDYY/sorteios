import requests

# Substitua 'YOUR_API_KEY' pela sua chave de API
api_key = '81ea7f503e3c4a3b911114040240912'
city = 'Itabira Minas Gerais'

url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

response = requests.get(url)
data = response.json()

return str(data)