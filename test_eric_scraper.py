# Write 10 tests of the function that scrapes the Centennial Campaign Impact.
import unittest
from unittest.mock import patch, Mock
from bs4 import BeautifulSoup
from eric_scraper import scrape_centennial_impact, parse_centennial_page, fetch_html



SAMPLE_HTML = """<html>
<head><title>Test Page</title></head>
<body>
<h1>Main Heading</h1>
<h2>Subheading 1</h2>
<p>This is a test paragraph.</p>
<a href="http://example.com">Example Link</a>

<h3>Subheading 2</h3>
<p>Another paragraph for testing.</p>
<a href="http://example.org">Another Link</a>
</body>
</html>"""

class TestEricScraper(unittest.TestCase):

    @patch('eric_scraper.requests.get')
    def test_fetch_html_returns_text(self, mock_get):
        mock_response = Mock()
        mock_response.text = "Hello, World!"
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = fetch_html("http://fakeurl.com")
        self.assertEqual(result, "Hello, World!")
        mock_response.raise_for_status.assert_called_once()

    @patch('eric_scraper.requests.get')
    def test_fetch_html_raises_http_error(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("HTTP Error")
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            fetch_html("http://fakeurl.com")

    def test_parse_centennial_page_headings(self):
        result = parse_centennial_page(SAMPLE_HTML)
        self.assertIn("Main Heading", result["headings"])
        self.assertIn("Subheading 1", result["headings"])
        self.assertIn("Subheading 2", result["headings"])

    def test_parse_centennial_page_paragraphs(self):
        result = parse_centennial_page(SAMPLE_HTML)
        self.assertIn("This is a test paragraph.", result["paragraphs"])
        self.assertIn("Another paragraph for testing.", result["paragraphs"])

    def test_parse_centennial_page_links(self):
        result = parse_centennial_page(SAMPLE_HTML)
        self.assertIn("Example Link", result["links"])
        self.assertIn("Another Link", result["links"])

    def test_parse_centennial_page_dedup(self):
        html = """<html><body>
        <h1>Heading</h1>
        <h1>Heading</h1>
        <p>Paragraph</p>
        <p>Paragraph</p>
        <a href="#">Link</a>
        <a href="#">Link</a>
        </body></html>"""
        result = parse_centennial_page(html)
        self.assertEqual(result["headings"], ["Heading"])
        self.assertEqual(result["paragraphs"], ["Paragraph"])
        self.assertEqual(result["links"], ["Link"])

    @patch('eric_scraper.fetch_html', return_value=SAMPLE_HTML)
    def test_scrape_centennial_impact_dict(self, mock_fetch):
        result = scrape_centennial_impact()
        self.assertIsInstance(result, dict)
        self.assertIn("headings", result)
        self.assertIn("paragraphs", result)
        self.assertIn("links", result)

    @patch('eric_scraper.fetch_html', return_value=SAMPLE_HTML)
    def test_scrape_centennial_impact_headings_content(self, mock_fetch):
        result = scrape_centennial_impact()
        self.assertIn("Main Heading", result["headings"])
    
    @patch('eric_scraper.fetch_html', return_value=SAMPLE_HTML)
    def test_scrape_centennial_impact_links_content(self, mock_fetch):
        result = scrape_centennial_impact()
        self.assertIn("Example Link", result["links"])

    def test_parse_empty_html(self):
        result = parse_centennial_page("<html></html>")
        self.assertEqual(result["headings"], [])
        self.assertEqual(result["paragraphs"], [])
        self.assertEqual(result["links"], [])

if __name__ == '__main__':
    unittest.main()

    