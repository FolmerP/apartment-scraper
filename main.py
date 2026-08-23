from scraper import get_current_listings
from storage import load_seen_ids, save_seen_ids
from notifier import notify

KEREBY_URL = "https://kereby.dk/bolig/"

def filter_by_budget(listings, max_rent):
    return [listing for listing in listings if listing["rent"] <= max_rent]

def run():
    seen = load_seen_ids()
    current = get_current_listings(KEREBY_URL)
    current = filter_by_budget(current, 12000)

    for listing in current:
        if listing["id"] not in seen:
            notify(listing)

    current_ids = {listing["id"] for listing in current}
    save_seen_ids(seen | current_ids)

if __name__ == "__main__":
    run()
