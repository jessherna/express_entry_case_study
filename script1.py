import requests
import json
import pandas as pd

json_url = 'https://www.canada.ca/content/dam/ircc/documents/json/ee_rounds_123_en.json'
response = requests.get(json_url)
json_data_string = response.text

json_data_dict = json.loads(json_data_string)
df = pd.DataFrame(json_data_dict['rounds'])