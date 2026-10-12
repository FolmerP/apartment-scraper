# Kereby Apartment Scraper

A small scraper that watches rental listings on [kereby.dk](https://kereby.dk/bolig/) and sends a push notification whenever a new apartment within budget appears.

## What it does

- Scrapes the current listings from Kereby.
- Keeps only the ones under a set monthly rent (currently 12,000 kr.).
- Compares them against the listings it has already seen, so the same one isn't reported twice.
- Sends a push notification (via [ntfy.sh](https://ntfy.sh)) for each new listing.
- Runs automatically every 10 minutes via GitHub Actions.

## How it's built

The code is split into modules, each with a single responsibility:

- **`scraper.py`** — fetches the page and parses the listing cards into dicts (`id`, `title`, `rent`) using BeautifulSoup.
- **`storage.py`** — loads and saves the set of already-seen listing IDs as JSON (`seen_listings.json`), so state survives between runs.
- **`notifier.py`** — sends a listing as a push notification to an ntfy topic.
- **`main.py`** — ties it together: load seen IDs, scrape, filter by budget, notify on anything new, save the updated set.

## How it runs

The scraper runs on **GitHub Actions** on a schedule (`*/10 * * * *`), and can also be triggered manually. Because each run starts on a fresh machine, the "seen listings" state is committed back to the repo as `seen_listings.json` at the end of each run. The ntfy topic is stored as a repository secret (`NTFY_TOPIC`) rather than hardcoded, so it isn't exposed in the public repo.

## Possible improvements

- Add error handling around the network calls, so a temporary outage on Kereby or ntfy doesn't fail the whole run.
- Make the budget and target URL configurable rather than hardcoded.
