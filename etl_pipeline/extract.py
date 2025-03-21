
import requests
import pandas as pd

def extract_weather_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=44.43&longitude=26.10&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['hourly'])
    return df
