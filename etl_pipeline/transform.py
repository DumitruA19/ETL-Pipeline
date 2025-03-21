
import pandas as pd


def clean_weather_data(df):
    df['time'] = pd.to_datetime(df['time'])
    df = df[df['temperature_2m'] > -50]
    return df
