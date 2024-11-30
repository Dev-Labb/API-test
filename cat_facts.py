import requests
from pprint import pprint
import pandas as pd

parameters = {'max_length': 200, 'limit': 10}
headers = {'content-type': 'application/json'}
r = requests.get('https://catfact.ninja/facts', params=parameters)
data = r.json()

df = pd.json_normalize(data)

pprint(df.data)

#pprint(data)

