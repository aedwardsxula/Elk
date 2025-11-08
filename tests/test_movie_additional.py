import unittest
import math
from movie_implementation import Movie


class TestMovieAdditional(unittest.TestCase):
    def test_constructor_with_float(self):
        m = Movie("A", 7.5, "Plot")
        self.assertIsInstance(m.rating, float)
        self.assertEqual(m.rating, 7.5)

    def test_constructor_with_int(self):
        m = Movie("B", 8, "Plot")
        self.assertIsInstance(m.rating, float)
        self.assertEqual(m.rating, 8.0)

    def test_constructor_with_string_convertible(self):
        m = Movie("C", "9.25", "Plot")
        self.assertIsInstance(m.rating, float)
        self.assertEqual(m.rating, 9.25)

    def test_constructor_with_string_nonconvertible_raises(self):
        with self.assertRaises(ValueError):
            Movie("D", "not-a-number", "Plot")

    def test_constructor_with_none_rating(self):
        m = Movie("E", None, "Plot")
        self.assertIsNone(m.rating)

    def test_constructor_with_bool_rating(self):
        m = Movie("F", True, "Plot")
        self.assertIsInstance(m.rating, float)
        self.assertEqual(m.rating, 1.0)

    def test_rating_nan(self):
        nan = float("nan")
        m = Movie("G", nan, "Plot")
        self.assertTrue(math.isnan(m.rating))

    def test_rating_inf(self):
        inf = float("inf")
        m = Movie("H", inf, "Plot")
        self.assertTrue(math.isinf(m.rating))
        self.assertGreater(m.rating, 0)

    def test_to_json_keys_and_values(self):
        m = Movie("I", 5, "Plot")
        d = m.to_json()
        self.assertIsInstance(d, dict)
        self.assertCountEqual(list(d.keys()), ["title", "rating", "plot"])
        self.assertEqual(d["title"], m.title)
        self.assertEqual(d["rating"], m.rating)
        self.assertEqual(d["plot"], m.plot)

    def test_to_json_returns_new_dict(self):
        m = Movie("K", 4.0, "Plot")
        d = m.to_json()
        d["title"] = "modified"
        d["rating"] = 0.0
        d["plot"] = "changed"
        # object should remain unchanged
        self.assertEqual(m.title, "K")
        self.assertEqual(m.rating, 4.0)
        self.assertEqual(m.plot, "Plot")

    def test_attribute_title_and_plot_modification(self):
        m = Movie("L", 3.5, "P")
        m.title = "New Title"
        m.plot = "New Plot"
        self.assertEqual(m.title, "New Title")
        self.assertEqual(m.plot, "New Plot")

    def test_attribute_rating_assignment_preserved(self):
        m = Movie("N", 7.0, "Plot")
        m.rating = 10  # direct assignment (should be preserved)
        self.assertEqual(m.rating, 10)

    def test_multiple_instances_independence(self):
        a = Movie("O", 1.0, "A")
        b = Movie("P", 2.0, "B")
        a.title = "Changed O"
        b.plot = "Changed B"
        self.assertEqual(a.title, "Changed O")
        self.assertEqual(b.plot, "Changed B")
        self.assertNotEqual(a.title, b.title)
        self.assertNotEqual(a.plot, b.plot)

    def test_empty_long_and_unicode_strings_allowed(self):
        cases = [
            ("", 0, ""),
            ("x" * 10000, 5, "p" * 20000),
            ("映画", 8.8, "プロット"),
        ]
        for title, rating, plot in cases:
            with self.subTest(title=title[:20], rating=rating):
                m = Movie(title, rating, plot)
                self.assertEqual(m.title, title)
                self.assertEqual(m.plot, plot)

    def test_rating_from_large_int(self):
        m = Movie("Q", 10**6, "Plot")
        self.assertEqual(m.rating, float(10**6))

    def test_constructor_with_empty_string_rating_raises(self):
        with self.assertRaises(ValueError):
            Movie("R", "", "Plot")

    def test_setting_rating_to_none_after_creation(self):
        m = Movie("S", 3.3, "Plot")
        m.rating = None
        self.assertIsNone(m.rating)

    def test_to_json_with_none_rating(self):
        m = Movie("T", None, "Plot")
        d = m.to_json()
        self.assertIsNone(d["rating"])

    def test_to_json_type_stability_with_mutations(self):
        m = Movie("U", 2.2, "Plot")
        d1 = m.to_json()
        d2 = m.to_json()
        # separate dict objects and same content
        self.assertIsNot(d1, d2)
        self.assertEqual(d1, d2)

    def test_rating_edge_cases_preserve_behavior(self):
        # ensure non-numeric types that convert raise/convert as expected
        with self.assertRaises(ValueError):
            Movie("V", " ", "Plot")
        m_bool = Movie("W", False, "Plot")
        self.assertEqual(m_bool.rating, 0.0)


if __name__ == "__main__":
    unittest.main()