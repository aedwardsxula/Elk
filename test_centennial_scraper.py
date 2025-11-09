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

    def test_contains_expected_keys(self):
        # Act
        keys = set(self.data.keys())
        # Assert
        self.assertTrue({"headings", "paragraphs", "links"}.issubset(keys))

    def test_has_headings_and_paragraphs(self):
        # Act
        headings = self.data["headings"]
        paragraphs = self.data["paragraphs"]
        # Assert
        self.assertGreater(len(headings), 0, "Expected at least one heading")
        self.assertGreater(len(paragraphs), 0, "Expected at least one paragraph")

    def test_first_heading_mentions_xavier(self):
        # Act
        first = (self.data["headings"][0] if self.data["headings"] else "").lower()
        # Assert
        self.assertIn("xavier", first, "First heading should mention 'Xavier'")

    # --------------- Unit tests (no network, fixture HTML) ---------------

    def test_parse_dedup_and_extraction_from_fixture(self):
        # Arrange
        html = """
        <html>
          <body>
            <h1>Xavier University of Louisiana</h1>
            <h2>Campaign Priorities</h2>
            <h2>Campaign Priorities</h2>
            <p>Impact paragraph one.</p>
            <p>Impact paragraph one.</p>
            <a href="/about">About</a>
            <a href="/about">About</a>
          </body>
        </html>
        """
        # Act
        parsed = parse_centennial_page(html)

        # Assert: correct keys
        self.assertTrue({"headings", "paragraphs", "links"}.issubset(parsed.keys()))
        # Assert: de-dup happened (only one of each duplicate remains)
        self.assertEqual(parsed["headings"].count("Campaign Priorities"), 1)
        self.assertEqual(parsed["paragraphs"].count("Impact paragraph one."), 1)
        self.assertEqual(parsed["links"].count("About"), 1)
        # Assert: types are lists of strings
        self.assertTrue(all(isinstance(x, str) for x in parsed["headings"]))
        self.assertTrue(all(isinstance(x, str) for x in parsed["paragraphs"]))
        self.assertTrue(all(isinstance(x, str) for x in parsed["links"]))

       

if __name__ == "__main__":
    unittest.main(verbosity=2)
