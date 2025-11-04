# Elk
tayjmcdile-alt, ausarkhan, apaiz12, ericbutler1209
<https://github.com/nishantsahoo/IMDB_Top50_Scrape>

Other Repo Choice Ranking:
1. <https://github.com/eliza-mat/n-ary-tree>
2. <https://github.com/sarthakbatragatech/AmazonScrapper>
3. <https://github.com/rudrajikadra/Web-Scraping-Amazon-Mens-Fashion-Search-Images-Beautiful-Soup-Python> (selected by Team Eagle)
4. <https://github.com/Reljod/Python-Data-Scraping-IMDb-Movie-site-using-BeautifulSoup-Series-1-> (selected by Team Echidna)
5. <https://github.com/aks060/ProtectFromPlagiarismChecker>

## Usage

Quick steps to create a virtual environment, install runtime dependencies, and run the scraper:

```bash
# create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# install runtime dependencies
pip install -r requirements.txt

# run the scraper (you'll be prompted for a year, e.g. 2019)
python final_scraper.py
```

Notes:
- The script writes a `debug.html` file (for diagnosing blocked or unexpected responses) and
	saves results into `DataSets/IMDB_Top_50_<year>.json` when successful.
- If you hit blocking or captchas from IMDB, try increasing delays or running from a different IP.

