import requests
from bs4 import BeautifulSoup
import json
import os


class MovieScraper:
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def scrape_movies(self, year):
        url = f"https://www.imdb.com/search/title/?title_type=feature&release_date={year}&sort=num_votes,desc&count=50"
        
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        movie_containers = soup.find_all('div', class_='lister-item-content')
        
        movies = []
        for i, container in enumerate(movie_containers, 1):
            movie_data = self.parse_movie_data(container, i)
            movies.append(movie_data)
        
        return movies
    
    def parse_movie_data(self, container, index):
        movie = {}
        
        # Get title
        title_element = container.find('h3', class_='lister-item-header')
        title = title_element.find('a').text.strip()
        movie['title'] = title
        
        # Get rating
        rating_element = container.find('div', class_='ratings-imdb-rating')
        rating = rating_element.get('data-value', 'N/A') if rating_element else 'N/A'
        movie['rating'] = rating
        
        # Get plot
        description = container.find_all('p', class_='text-muted')
        plot = description[1].text.strip() if len(description) > 1 else "No description available"
        movie['plot'] = plot
        
        return movie
