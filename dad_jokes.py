import json
import requests
from pprint import pprint
import pandas as pd
response = requests.get('https://icanhazdadjoke.com/', headers= {'Accept': 'application/json'})
data = response.json()




pprint(data)