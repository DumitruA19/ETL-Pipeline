
from etl_pipeline.extract import extract_weather_data
from etl_pipeline.transform import clean_weather_data
from etl_pipeline.load import load_to_blob

def run_etl():
    df_raw = extract_weather_data()
    df_clean = clean_weather_data(df_raw)
    load_to_blob(df_clean)

if __name__ == "__main__":
    run_etl()
