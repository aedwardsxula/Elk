import requests
from bs4 import BeautifulSoup
import json
import os
import re
from time import sleep
from urllib.parse import urlparse


def _sanitize_filename(s: str) -> str:
    return re.sub(r'[^A-Za-z0-9_.-]', '_', s)


def scrape_centennial(url: str, session: requests.Session = None, max_items: int = 200):
    """Fetch a page and try to extract event-like items for a Centennial/homecoming page.

    This is intentionally conservative and generic: it looks for common event containers
    (.event, .event-item, .event-list, li under main content) and extracts title/date/desc.

    Returns a list of dicts with keys: title, date, description, url
    Saves results to DataSets/Centennial_<host>.json and returns the list.
    """
    if session is None:
        session = requests.Session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; CentennialTester/1.0; +https://example.com)'
    }

    resp = session.get(url, headers=headers, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, 'html.parser')

    # Try common selectors for event items
    selectors = [
        '.event', '.event-item', '.event-listing', '.event-list li',
        '.listing .item', '.list-item', '.card.event', 'article.event'
    ]

    items = []
    for sel in selectors:
        found = soup.select(sel)
        if found:
            items = found
            break

    # fallback: find list items in main content
    if not items:
        main = soup.find('main') or soup.find(id='content') or soup
        items = main.find_all('li')[:max_items]

    results = []
    for el in items[:max_items]:
        # title: prefer headings or link text
        title = None
        for tag in ('h1', 'h2', 'h3', 'h4'):
            t = el.find(tag)
            if t and t.get_text(strip=True):
                title = t.get_text(strip=True)
                break

        if not title:
            a = el.find('a')
            if a and a.get_text(strip=True):
                title = a.get_text(strip=True)

        text = el.get_text(separator=' ', strip=True)

        # date: look for time tag or date-like patterns
        date = None
        time_tag = el.find('time')
        if time_tag and time_tag.get_text(strip=True):
            date = time_tag.get_text(strip=True)
        else:
            m = re.search(r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d{1,2}(?:,\s*\d{4})?', text)
            if m:
                date = m.group(0)

        # description: first paragraph
        desc = None
        p = el.find('p')
        if p and p.get_text(strip=True):
            desc = p.get_text(strip=True)
        else:
            # use truncated text
            desc = (text[:300] + '...') if len(text) > 300 else text

        # url: absolute link if present
        link = el.find('a')
        link_url = None
        if link and link.get('href'):
            link_url = link.get('href')
            if link_url.startswith('/'):
                parsed = urlparse(url)
                link_url = f"{parsed.scheme}://{parsed.netloc}{link_url}"

        if not title and not desc:
            continue

        results.append({'title': title or desc[:80], 'date': date, 'description': desc, 'url': link_url})

    # Save output
    parsed = urlparse(url)
    host = parsed.netloc.replace(':', '_')
    if not os.path.exists('DataSets'):
        os.makedirs('DataSets')

    out_file = os.path.join('DataSets', f'Centennial_{_sanitize_filename(host)}.json')
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Tester: scrape a Centennial/homecoming page')
    parser.add_argument('--url', '-u', required=True, help='URL of the Centennial page to scrape')
    args = parser.parse_args()

    print('Scraping', args.url)
    try:
        data = scrape_centennial(args.url)
        print(f'Found {len(data)} items. Saved to DataSets/')
    except Exception as e:
        print('Error scraping:', e)


if __name__ == '__main__':
    main()
