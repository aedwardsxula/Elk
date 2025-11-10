import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from movie_scraper_implementation import MovieScraper


class TestMovieScraper(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.scraper = MovieScraper()
    
    def test_init(self):
        """Test MovieScraper initialization."""
        self.assertIsInstance(self.scraper, MovieScraper)
        self.assertIn('User-Agent', self.scraper.headers)
        self.assertEqual(self.scraper.headers['User-Agent'], 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    
    @patch('movie_scraper_implementation.requests.get')
    def test_scrape_movies_success(self, mock_get):
        """Test successful movie scraping."""
        # Mock HTML response
        mock_html = '''
        <div class="lister-item-content">
            <h3 class="lister-item-header">
                <a>Test Movie 1</a>
            </h3>
            <div class="ratings-imdb-rating" data-value="8.5"></div>
            <p class="text-muted">Genre info</p>
            <p class="text-muted">This is a test plot for movie 1.</p>
        </div>
        <div class="lister-item-content">
            <h3 class="lister-item-header">
                <a>Test Movie 2</a>
            </h3>
            <div class="ratings-imdb-rating" data-value="7.2"></div>
            <p class="text-muted">Genre info</p>
            <p class="text-muted">This is a test plot for movie 2.</p>
        </div>
        '''
        
        mock_response = MagicMock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response
        
        result = self.scraper.scrape_movies(2020)
        
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['title'], 'Test Movie 1')
        self.assertEqual(result[0]['rating'], '8.5')
        self.assertEqual(result[1]['title'], 'Test Movie 2')
        self.assertEqual(result[1]['rating'], '7.2')
    
    def test_parse_movie_data_with_valid_container(self):
        """Test parsing movie data from valid HTML container."""
        html = '''
        <div class="lister-item-content">
            <h3 class="lister-item-header">
                <a>The Amazing Movie</a>
            </h3>
            <div class="ratings-imdb-rating" data-value="9.1"></div>
            <p class="text-muted">Genre: Action, Drama</p>
            <p class="text-muted">An incredible story about heroes and villains.</p>
        </div>
        '''
        
        soup = BeautifulSoup(html, 'html.parser')
        container = soup.find('div', class_='lister-item-content')
        
        result = self.scraper.parse_movie_data(container, 1)
        
        self.assertEqual(result['title'], 'The Amazing Movie')
        self.assertEqual(result['rating'], '9.1')
        self.assertEqual(result['plot'], 'An incredible story about heroes and villains.')
    
    def test_parse_movie_data_missing_rating(self):
        """Test parsing movie data when rating is missing."""
        html = '''
        <div class="lister-item-content">
            <h3 class="lister-item-header">
                <a>Movie Without Rating</a>
            </h3>
            <p class="text-muted">Genre: Comedy</p>
            <p class="text-muted">A funny movie with no rating.</p>
        </div>
        '''
        
        soup = BeautifulSoup(html, 'html.parser')
        container = soup.find('div', class_='lister-item-content')
        
        result = self.scraper.parse_movie_data(container, 1)
        
        self.assertEqual(result['title'], 'Movie Without Rating')
        self.assertEqual(result['rating'], 'N/A')
        self.assertEqual(result['plot'], 'A funny movie with no rating.')
    
    def test_parse_movie_data_missing_plot(self):
        """Test parsing movie data when plot description is missing."""
        html = '''
        <div class="lister-item-content">
            <h3 class="lister-item-header">
                <a>Movie Without Plot</a>
            </h3>
            <div class="ratings-imdb-rating" data-value="6.8"></div>
            <p class="text-muted">Genre: Horror</p>
        </div>
        '''
        
        soup = BeautifulSoup(html, 'html.parser')
        container = soup.find('div', class_='lister-item-content')
        
        result = self.scraper.parse_movie_data(container, 1)
        
        self.assertEqual(result['title'], 'Movie Without Plot')
        self.assertEqual(result['rating'], '6.8')
        self.assertEqual(result['plot'], 'No description available')
    
    @patch('movie_scraper_implementation.requests.get')
    def test_scrape_movies_url_construction(self):
        """Test that the correct URL is constructed and called."""
        mock_response = MagicMock()
        mock_response.text = '<div class="lister-item-content"></div>'
        
        with patch('movie_scraper_implementation.requests.get') as mock_get:
            mock_get.return_value = mock_response
            
            self.scraper.scrape_movies(2021)
            
            expected_url = "https://www.imdb.com/search/title/?title_type=feature&release_date=2021&sort=num_votes,desc&count=50"
            mock_get.assert_called_once_with(expected_url, headers=self.scraper.headers)
    
    @patch('movie_scraper_implementation.requests.get')
    def test_scrape_movies_empty_results(self):
        """Test handling when no movie containers are found."""
        mock_response = MagicMock()
        mock_response.text = '<html><body>No movies found</body></html>'
        
        with patch('movie_scraper_implementation.requests.get') as mock_get:
            mock_get.return_value = mock_response
            
            result = self.scraper.scrape_movies(1900)
            
            self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
