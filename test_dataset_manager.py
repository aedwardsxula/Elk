from dataset_manager import DataSetManager
import unittest
import os
import csv  
import tempfile

#10 unit tests for dataset_manager.py

class TestDataSetManager(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.manager = DataSetManager(self.temp_dir.name)
        self.sample_movies = [
            {'title': 'Movie A', 'year': '2020', 'rating': '8.5', 'genre': 'Drama'},
            {'title': 'Movie B', 'year': '2019', 'rating': '7.2', 'genre': 'Comedy'}
        ]


    def tearDown(self):
        # Clean up test files
        self.temp_dir.cleanup()

    def test_init_creates_base_dir(self):
        self.assertTrue(os.path.exists(self.temp_dir.name))


    def test_save_movies_creates_csv_file(self):
        filename = 'test_movies.csv'
        self.manager.save_movies(self.sample_movies, filename)
        filepath = os.path.join(self.temp_dir.name, filename)
        self.assertTrue(os.path.isfile(filepath))
    
    def test_csv_header_written(self):
        filename = 'test_movies.csv'
        self.manager.save_movies(self.sample_movies, filename)
        filepath = os.path.join(self.temp_dir.name, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ['title', 'year', 'rating', 'genre'])

    def test_load_returns_same_length(self):
        filename = 'test_movies.csv'
        self.manager.save_movies(self.sample_movies, filename)
        loaded_movies = self.manager.load_movies(filename)
        self.assertEqual(len(loaded_movies), len(self.sample_movies))

    def test_save_and_load_match(self):
        filename = 'test_movies.csv'
        self.manager.save_movies(self.sample_movies, filename)
        loaded_movies = self.manager.load_movies(filename)
        self.assertEqual(loaded_movies, self.sample_movies)

    def test_save_empty_list(self):
        filename = 'empty_movies.csv'
        self.manager.save_movies([], filename)
        filepath = os.path.join(self.temp_dir.name, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            self.assertEqual(len(rows), 1)  
    
    def test_load_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            self.manager.load_movies('non_existent_file.csv')

    def test_multiple_files(self):
        filename1 = 'movies1.csv'
        filename2 = 'movies2.csv'
        self.manager.save_movies(self.sample_movies, filename1)
        self.manager.save_movies(self.sample_movies, filename2)
        loaded1 = self.manager.load_movies(filename1)
        loaded2 = self.manager.load_movies(filename2)
        self.assertEqual(loaded1, loaded2)

    def test_save_invalid_data_type(self):
        filename = 'invalid_movies.csv'
        with self.assertRaises(TypeError):
            self.manager.save_movies("This is not a list", filename)

    def test_fieldnames_in_csv(self):
        filename = 'test_movies.csv'
        self.manager.save_movies(self.sample_movies, filename)
        filepath = os.path.join(self.temp_dir.name, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.assertEqual(reader.fieldnames, ['title', 'year', 'rating', 'genre'])

    def test_get_dataset_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            self.manager.get_dataset()

if __name__ == '__main__':
    unittest.main()       
