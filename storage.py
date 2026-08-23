import os
import json

def load_seen_ids():
    if not os.path.exists("seen_listings.json"):
        return set()

    with open("seen_listings.json") as f:
        ids_list = json.load(f)

    return set(ids_list)

def save_seen_ids(ids):
    ids_list = list(ids)

    with open("seen_listings.json", "w") as f:
        json.dump(ids_list, f)
