#UML Class: DataSetManager
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
       if not isinstance(movies, list):
           raise TypeError("Movies should be a list of dictionaries.")
       
       filepath = os.path.join(self.base_dir, filename)
       fieldnames = ['title', 'year', 'rating', 'genre']

       with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for movie in movies:
                if not isinstance(movie, dict):
                    raise TypeError("Each movie should be a dictionary.")
                writer.writerow(movie)


   def load_movies(self, filename):
       filepath = os.path.join(self.base_dir, filename)
       movies = []
       with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
           reader = csv.DictReader(csvfile)
           for row in reader:
               movies.append(row)
       return movies
