"""Movie class implemented exactly as in the UML diagram.

Fields:
- title: str
- rating: float
- plot: str

Methods:
- to_json() -> dict

Do not add or remove attributes or behavior without an updated UML diagram.
"""

from __future__ import annotations

from typing import Dict


class Movie:
    """Simple Movie value object matching the UML.

    Attributes are public and typed exactly as specified by the UML.
    """

    def __init__(self, title: str, rating: float, plot: str) -> None:
        self.title: str = title
        self.rating: float = float(rating) if rating is not None else None
        self.plot: str = plot

    def to_json(self) -> Dict[str, object]:
        """Return a dict representation of the Movie.

        Keys match the UML attribute names: title, rating, plot.
        """
        return {
            "title": self.title,
            "rating": self.rating,
            "plot": self.plot,
        }
