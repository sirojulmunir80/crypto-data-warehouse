import requests
import pandas as pd

def extract_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    