from dotenv import load_dotenv
load_dotenv()

from azure.storage.blob import BlobServiceClient
from io import StringIO
import os

def load_to_blob(df):
    
    connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")
    file_name = "weather_data.csv"

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    blob_client.upload_blob(csv_buffer.getvalue(), overwrite=True)
