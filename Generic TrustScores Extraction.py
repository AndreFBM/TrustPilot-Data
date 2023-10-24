import requests
import pandas as pd
from datetime import datetime
import urllib.request
from sqlalchemy import create_engine

# API details
BASE_URL = "https://api.trustpilot.com/v1/business-units/"
HEADERS = {"apikey": "YOUR_API_KEY_HERE"}

# Market IDs
markets = [
    # Your market IDs here...
]

# Extract data from API
data = []
for market_id in markets:
    response = requests.get(BASE_URL + market_id, headers=HEADERS)
    if response.status_code == 200:
        json_data = response.json()
        data.append({
            "Market_id": json_data["id"],
            "country": json_data["country"],
            "Domain": json_data["name"]["identifying"],
            "trustScore": json_data["score"]["trustScore"]
        })
    else:
        print(f"Failed to fetch data for market ID: {market_id}")

df = pd.DataFrame(data)

current_time = datetime.now()
df['UpdateDate'] = current_time

# DB connection details
CONNECTION_STRING = (
    "DRIVER={YOUR_DRIVER_HERE};"
    "SERVER=YOUR_SERVER_HERE;"
    "DATABASE=YOUR_DATABASE_HERE;"
    "UID=YOUR_USERNAME_HERE;"
    "PWD=YOUR_PASSWORD_HERE;"
)
quoted = urllib.parse.quote_plus(CONNECTION_STRING)
engine = create_engine(f'mssql+pyodbc:///?odbc_connect={quoted}')

table_name = "YOUR_TABLE_NAME_HERE"
df.to_sql(table_name, schema='YOUR_SCHEMA_HERE', con=engine, if_exists='replace', index=False)
engine.dispose()

print(f"DataFrame inserted into '{table_name}' table in SQL Server.")
