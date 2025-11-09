import unittest
from centennial_scraper import scrape_centennial_impact

class TestCentennialScraper(unittest.TestCase):

    def test_returns_dict(self):
        """Test that the scraper returns a dictionary."""
        result = scrape_centennial_impact()
        self.assertIsInstance(result, dict)

    def test_contains_expected_keys(self):
        """Test that expected keys appear in the result."""
        data = scrape_centennial_impact()
        expected_keys = {"headings", "paragraphs", "links"}
        self.assertTrue(expected_keys.issubset(data.keys()))

    def test_has_headings_and_paragraphs(self):
        """Test that the scraper finds at least one heading and paragraph."""
        data = scrape_centennial_impact()
        self.assertGreater(len(data["headings"]), 0)
        self.assertGreater(len(data["paragraphs"]), 0)

    def test_returns_dict_for_multiple_calls(self):
        """Test scraper stability across multiple calls."""
        first = scrape_centennial_impact()
        second = scrape_centennial_impact()
        self.assertIsInstance(first, dict)
        self.assertIsInstance(second, dict)

    def test_values_are_lists(self):
        """Ensure the values returned are lists."""
        data = scrape_centennial_impact()
        for key in ["headings", "paragraphs", "links"]:
            self.assertIsInstance(data[key], list)

if __name__ == "__main__":
    unittest.main()


       


