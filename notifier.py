import os
from urllib.request import Request, urlopen

NTFY_TOPIC = os.environ["NTFY_TOPIC"]

def notify(listing):
    message = f"{listing['title']} - {listing['rent']} kr./md"
    url = f"https://ntfy.sh/{NTFY_TOPIC}"

    req = Request(url, data=message.encode("utf-8"), method="POST")
    urlopen(req)
