"""Comprehensive unit tests for the Movie class."""

import unittest
from movie import Movie


class TestMovie(unittest.TestCase):
    """Test cases for the Movie class."""

    def test_init_with_valid_string_rating(self):
        """Test Movie initialization with string rating that can be converted to float."""
        movie = Movie("The Shawshank Redemption", "9.3", "Two imprisoned men bond over a number of years.")
        
        self.assertEqual(movie.title, "The Shawshank Redemption")
        self.assertEqual(movie.rating, 9.3)
        self.assertIsInstance(movie.rating, float)
        self.assertEqual(movie.plot, "Two imprisoned men bond over a number of years.")

    def test_init_with_float_rating(self):
        """Test Movie initialization with float rating."""
        movie = Movie("The Godfather", 9.2, "The aging patriarch of an organized crime dynasty transfers control.")
        
        self.assertEqual(movie.title, "The Godfather")
        self.assertEqual(movie.rating, 9.2)
        self.assertIsInstance(movie.rating, float)
        self.assertEqual(movie.plot, "The aging patriarch of an organized crime dynasty transfers control.")

    def test_init_with_integer_rating(self):
        """Test Movie initialization with integer rating."""
        movie = Movie("Pulp Fiction", 8, "The lives of two mob hitmen intertwine.")
        
        self.assertEqual(movie.title, "Pulp Fiction")
        self.assertEqual(movie.rating, 8.0)
        self.assertIsInstance(movie.rating, float)
        self.assertEqual(movie.plot, "The lives of two mob hitmen intertwine.")

    def test_init_with_none_rating(self):
        """Test Movie initialization with None rating."""
        movie = Movie("Unrated Movie", None, "A movie without a rating.")
        
        self.assertEqual(movie.title, "Unrated Movie")
        self.assertIsNone(movie.rating)
        self.assertEqual(movie.plot, "A movie without a rating.")

    def test_init_with_empty_strings(self):
        """Test Movie initialization with empty strings."""
        movie = Movie("", 0.0, "")
        
        self.assertEqual(movie.title, "")
        self.assertEqual(movie.rating, 0.0)
        self.assertEqual(movie.plot, "")

    def test_init_with_very_long_strings(self):
        """Test Movie initialization with very long strings."""
        long_title = "A" * 1000
        long_plot = "B" * 5000
        movie = Movie(long_title, 7.5, long_plot)
        
        self.assertEqual(movie.title, long_title)
        self.assertEqual(movie.rating, 7.5)
        self.assertEqual(movie.plot, long_plot)

    def test_to_json_returns_correct_dict(self):
        """Test that to_json returns a dictionary with correct keys and values."""
        movie = Movie("Inception", 8.8, "A thief who steals corporate secrets through dream-sharing technology.")
        json_data = movie.to_json()
        
        self.assertIsInstance(json_data, dict)
        self.assertEqual(len(json_data), 3)
        self.assertIn("title", json_data)
        self.assertIn("rating", json_data)
        self.assertIn("plot", json_data)
        
        self.assertEqual(json_data["title"], "Inception")
        self.assertEqual(json_data["rating"], 8.8)
        self.assertEqual(json_data["plot"], "A thief who steals corporate secrets through dream-sharing technology.")

    def test_to_json_with_none_rating(self):
        """Test to_json method when rating is None."""
        movie = Movie("Unknown Rating", None, "A mystery movie.")
        json_data = movie.to_json()
        
        self.assertIsInstance(json_data, dict)
        self.assertEqual(json_data["title"], "Unknown Rating")
        self.assertIsNone(json_data["rating"])
        self.assertEqual(json_data["plot"], "A mystery movie.")

    def test_attribute_modification_after_creation(self):
        """Test that Movie attributes can be modified after object creation."""
        movie = Movie("Original Title", 5.0, "Original plot")
        
        # Modify attributes
        movie.title = "Modified Title"
        movie.rating = 7.5
        movie.plot = "Modified plot"
        
        # Verify modifications
        self.assertEqual(movie.title, "Modified Title")
        self.assertEqual(movie.rating, 7.5)
        self.assertEqual(movie.plot, "Modified plot")
        
        # Verify to_json reflects the changes
        json_data = movie.to_json()
        self.assertEqual(json_data["title"], "Modified Title")
        self.assertEqual(json_data["rating"], 7.5)
        self.assertEqual(json_data["plot"], "Modified plot")

    def test_multiple_movie_objects_independence(self):
        """Test that multiple Movie objects maintain their independence."""
        movie1 = Movie("Movie One", 6.0, "First movie plot")
        movie2 = Movie("Movie Two", 8.0, "Second movie plot")
        
        # Verify initial state
        self.assertEqual(movie1.title, "Movie One")
        self.assertEqual(movie2.title, "Movie Two")
        
        # Modify one movie
        movie1.title = "Modified Movie One"
        movie1.rating = 9.0
        
        # Verify that only movie1 was affected
        self.assertEqual(movie1.title, "Modified Movie One")
        self.assertEqual(movie1.rating, 9.0)
        self.assertEqual(movie2.title, "Movie Two")
        self.assertEqual(movie2.rating, 8.0)
        
        # Verify to_json for both movies
        json1 = movie1.to_json()
        json2 = movie2.to_json()
        
        self.assertEqual(json1["title"], "Modified Movie One")
        self.assertEqual(json1["rating"], 9.0)
        self.assertEqual(json2["title"], "Movie Two")
        self.assertEqual(json2["rating"], 8.0)


if __name__ == "__main__":
    unittest.main()