import requests
import os
from dotenv import load_dotenv
import json

api_url = "https://api.api-ninjas.com/v1/quotes"
load_dotenv()
api_key = os.environ.get("api_key")
headers = {'X-Api-Key': api_key}

response = requests.get(api_url, headers)
if response.status_code == requests.codes.ok:
	result = json.loads(response.text)
	print(f'Quote: {result[0]["quote"]}\nAuthor: {result[0]["author"]}\nCategory: {result[0]["category"]}')
else:
	print(f"ERROR: {response.status_code}, {response.text}")
