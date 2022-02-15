import requests

ngrok_url = 'https://53d1-2600-1700-eee0-1ca0-ecd0-9305-ffb3-64d5.ngrok.io'
endpoint = f'{ngrok_url}/box-office-mojo-scraper'

r = requests.post(endpoint, json={})
print(r.text)