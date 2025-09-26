import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def fetch_foot_traffic(lat, long):
    api_key = os.getenv("FOURSQUARE_API_KEY")

    if not api_key:
        return None
    
    url = "https://places-api.foursquare.com/places/search"
    headers = {
        "Authorization": "Bearer " + api_key,
        "accept": "application/json",
        "X-Places-Api-Version": "2025-06-17"
    }

    resp = requests.get(
        url, params={"ll": f"{lat},{long}", "radius": 200, "fsq_category_ids": "52f2ab2ebcbc57f1066b8b33", "tel_format": "NATIONAL", "fields": "popularity,rating,stats,email,tel,wbesite"}, headers=headers, timeout=60
    )

    resp.raise_for_status()
    data = resp.json()
    print(data)

if __name__ == "__main__":
    fetch_foot_traffic(37.8981884, -122.0580511) 
