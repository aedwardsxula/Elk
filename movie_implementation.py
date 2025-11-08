from __future__ import annotations

from typing import Dict, Optional


class Movie:
    """Simple Movie value object matching the UML.

    Attributes are public and typed exactly as specified by the UML.
    """

    def __init__(self, title: str, rating: Optional[float], plot: str) -> None:
        self.title: str = title

        if rating is None:
            self.rating: Optional[float] = None
        else:
            # Strings: empty string is invalid, non-convertible raises ValueError
            if isinstance(rating, str):
                if rating == "":
                    raise ValueError("rating cannot be empty string")
                try:
                    self.rating = float(rating)
                except ValueError:
                    raise ValueError("rating string must be convertible to float")
            else:
                # ints, bools, floats -> convert to float
                self.rating = float(rating)

        self.plot: str = plot

    def to_json(self) -> Dict[str, object]:
        """Return a dict representation of the Movie."""
        return {"title": self.title, "rating": self.rating, "plot": self.plot}