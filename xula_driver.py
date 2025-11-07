from eric_scraper import scrape_centennial_impact

def main():
    print("Running Centennial Scraper...")
    data = scrape_centennial_impact()
    print("Scraper Output:")
    print(data)

if __name__ == "__main__":
    main()
