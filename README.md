
# Weather ETL Pipeline ☁️

Un ETL simplu care:

- Extrage date meteo din Open-Meteo API
- Le curăță
- Le încarcă într-un Azure Blob Storage

## Setup

1. Creează un `.env` sau setează variabile de mediu:

```
AZURE_STORAGE_CONNECTION_STRING=your_connection_string
AZURE_STORAGE_CONTAINER_NAME=your_container_name
```

2. Rulează local:
```bash
pip install -r requirements.txt
python etl_pipeline/main.py
```

3. Deploy pe Azure Functions (opțional)
