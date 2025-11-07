# UML Class: DataSetManager
#Base_dir: str
#save_movies(movies, filename)
#load_movies(filename)
#movies: IMDB_Top_50_2016.json

import os
import csv

class DataSetManager:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        os.makedirs(base_dir, exist_ok=True)
        

    def save_movies(self, movies, filename):
        filepath = os.path.join(self.base_dir, filename)
        with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['title', 'year', 'rating', 'genre']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for movie in movies:
                writer.writerow(movie)

    def load_movies(self, filename):
        filepath = os.path.join(self.base_dir, filename)
        movies = []
        with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                movies.append(row)
        return movies