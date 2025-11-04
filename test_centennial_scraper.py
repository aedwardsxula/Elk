# test_centennial_scraper.py
import unittest
from eric_scraper import (
    scrape_centennial_impact,
    parse_centennial_page,
)

class TestCentennialScraper(unittest.TestCase):
    def setUp(self):
        # Arrange (integration): run the real scraper once
        self.data = scrape_centennial_impact()

    # ---------------- Integration tests (live page) ----------------

    def test_returns_dict(self):
        # Act
        result = self.data
        # Assert
        self.assertIsInstance(result, dict, "Scraper should return a dict")
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
