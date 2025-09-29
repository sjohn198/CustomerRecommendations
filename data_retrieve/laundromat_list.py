import pandas as pd
import requests

def fetch_overpass_nodes():
    query = """
        [out:json][timeout:25];

        area["ISO3166-2"="US-CA"]->.searchArea;
        (
        node["shop"="laundry"](area.searchArea);
        way["shop"="laundry"](area.searchArea);
        relation["shop"="laundry"](area.searchArea);
        node["amenity"="laundry"](area.searchArea);
        way["amenity"="laundry"](area.searchArea);
        relation["amenity"="laundry"](area.searchArea);
        );

        out center;
    """

    url = "https://overpass-api.de/api/interpreter"

    response = requests.get(url, params={"data": query}, timeout=60)
    response.raise_for_status()
    data = response.json()

    items = []
    max_count = 100000
    cur_count = 0
    print(len(data.get("elements", [])))
    print(data.get("elements", [])[0])
    # for element in data.get("elements", []):
    #     print(element)