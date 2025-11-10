from centennial_scraper import scrape_centennial_impact
from movie_implementation import Movie          # Movie class from UML lives in its own module
from dataset_manager import DatasetManager      # DatasetManager class from UML


def main() -> None:
    # ---------- Centennial Scraper ----------
    print("Running Centennial Scraper...")
    data = scrape_centennial_impact()
    print("Scraper Output:")
    print(data)

    print("\n-----------------------------------------\n")

    # ---------- Movie (UML) ----------
    print("This is the Movie class from the UML diagram:")
    movie_example = Movie(
        title="Inception",
        rating=8.8,
        plot="A skilled thief enters dreams to steal secrets."
    )
    print("Movie Title:", movie_example.title)
    print("Movie Rating:", movie_example.rating)
    print("Movie Plot:", movie_example.plot)
    print("Movie as JSON:", movie_example.to_json())

    print("\n-----------------------------------------\n")

    # ---------- DatasetManager (UML) ----------
    print("This is the DatasetManager class from the UML diagram:")
    dm = DatasetManager()

    # These calls are wrapped so the driver won't crash if the
    # methods are stubs or not fully implemented yet.
    try:
        loaded = dm.load_data()
        print("Loaded Data:", loaded)
    except Exception as e:
        print("load_data() raised:", e)

    try:
        dataset = dm.get_dataset()
        print("Dataset:", dataset)
    except Exception as e:
        print("get_dataset() raised:", e)


if __name__ == "__main__":
    main()
