import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

def fetch_fsq_info(lat, long):
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
        url, params={"ll": f"{lat},{long}", "radius": 200, "fsq_category_ids": "52f2ab2ebcbc57f1066b8b33", "tel_format": "NATIONAL", "fields": "popularity,rating,stats,email,tel,website"}, headers=headers, timeout=1
    )

    resp.raise_for_status()
    data = resp.json()
    return data

# if __name__ == "__main__":
#     fetch_foot_traffic(37.8981884, -122.0580511) 
