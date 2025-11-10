from typing import Dict


class Movie:
    """Movie class with basic movie information and accessor methods."""

    def __init__(self, title: str, rating: float, plot: str) -> None:
        """Initialize Movie with title, rating, and plot."""
        self.title = title
        self.rating = rating
        self.plot = plot

    def get_title(self) -> str:
        """Return the movie title."""
        return self.title

    def get_year(self) -> str:
        """Return the movie year (placeholder implementation)."""
        return "Unknown"

    def get_genre(self) -> str:
        """Return the movie genre (placeholder implementation)."""
        return "Unknown"

    def get_rating(self) -> float:
        """Return the movie rating."""
        return self.rating

    def to_json(self) -> Dict:
        """Return a dictionary representation of the Movie."""
        return {
            "title": self.title,
            "rating": self.rating,
            "plot": self.plot
        }