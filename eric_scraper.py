# eric_scraper.py
import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Tuple

URL = "https://www.xula.edu/about/centennial.html"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

def fetch_html(url: str = URL, timeout: int = 15) -> str:
    r = requests.get(url, headers=HEADERS, timeout=timeout)
    r.raise_for_status()
    return r.text

def parse_centennial_page(html: str) -> Dict[str, List[str]]:
    """
    Return a dict with headings, paragraphs, and links (text only).
    """
    soup = BeautifulSoup(html, "html.parser")

    # Some XULA pages use Divi/ET Builder blocks; keep both generic + block-specific grabs.
    container_selectors = [
        "div.et_pb_text_inner",
        "main",              # generic fallback
        "article",           # generic fallback
        "div#main-content",  # generic fallback
    ]
    containers = []
    for sel in container_selectors:
        containers.extend(soup.select(sel))
    if not containers:
        containers = [soup]  # fallback: parse whole doc

    def collect_text(nodes, tag: str) -> List[str]:
        out = []
        for n in nodes:
            for t in n.find_all(tag):
                text = t.get_text(" ", strip=True)
                if text:
                    out.append(text)
        return out

    headings = []
    for htag in ("h1", "h2", "h3"):
        headings.extend(collect_text(containers, htag))

    # paragraphs
    paragraphs = collect_text(containers, "p")

    # links (text only here; add hrefs if you want)
    links_text = []
    for n in containers:
        for a in n.find_all("a"):
            txt = a.get_text(" ", strip=True)
            if txt:
                links_text.append(txt)

    # de-dup while preserving order
    def dedup(seq: List[str]) -> List[str]:
        seen = set()
        out = []
        for s in seq:
            if s not in seen:
                seen.add(s)
                out.append(s)
        return out

    return {
        "headings": dedup(headings),
        "paragraphs": dedup(paragraphs),
        "links": dedup(links_text),
    }

def scrape_centennial_impact() -> Dict[str, List[str]]:
    """High-level function your driver/tests can call."""
    html = fetch_html(URL)
    return parse_centennial_page(html)

if __name__ == "__main__":
    data = scrape_centennial_impact()
    print(f"Headings: {len(data['headings'])}")
    for h in data["headings"][:5]:
        print("  •", h)
    print(f"\nParagraphs: {len(data['paragraphs'])}")
    for p in data["paragraphs"][:3]:
        print("  •", p[:120], "...")
    print(f"\nLinks: {len(data['links'])}")
    for l in data["links"][:5]:
        print("  •", l)
