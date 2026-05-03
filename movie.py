import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MOVIE_FILE = os.path.join(BASE_DIR, "movies.txt")

def load_movies():
    movies = []
    try:
        with open(MOVIE_FILE, "r") as f:
            next(f)  # skip header line
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    movies.append({
                        "title": parts[0],
                        "hall": parts[1],
                        "start": parts[2],
                        "end": parts[3],
                    })
    except FileNotFoundError:
        print("Error: movies.txt not found.")
    return movies

def display_movies(movies):
    print("\n========================================")
    print("             NOW SHOWING")
    print("========================================")
    for i, m in enumerate(movies, 1):
        print(f"{i}. {m['title']}")
        print(f"   Hall {m['hall']} | {m['start']} - {m['end']}")
    print("----------------------------------------")

def add_movie():
    print("\n--- Add New Movie ---")
    title = input("Movie title: ")
    hall = input("Hall (A/B/C): ").upper()

    while hall not in ['A', 'B', 'C']:
        print("Invalid hall. Please enter A, B, or C.")
        hall = input("Hall (A/B/C): ").upper()

    start = input("Start time (e.g. 14:00): ")
    end = input("End time (e.g. 16:40): ")

    with open(MOVIE_FILE, "a") as f:
        with open(MOVIE_FILE, "r") as check:
            content = check.read()
            if content and not content.endswith("\n"):
                f.write("\n") 
        f.write(f"{title},{hall},{start},{end}\n")

    # create layout file for this showtime
    import os
    layout_file = f"layouts/layout_{hall}_{start.replace(':', '')}.txt"
    if not os.path.exists(layout_file):
        with open(layout_file, "w") as f:
            for _ in range(6):
                f.write("O,O,O,O,O,O,O,O\n")
        print(f"Layout file created for Hall {hall} at {start}.")

    print(f"\n'{title}' added successfully!")

def delete_movie():
    movies = load_movies()
    if not movies:
        print("No movies to delete.")
        return

    display_movies(movies)

    while True:
        try:
            choice = int(input("\nSelect movie number to delete: "))
            if 1 <= choice <= len(movies):
                removed = movies.pop(choice - 1)
                break
            else:
                print(f"Please enter a number between 1 and {len(movies)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # rewrite movies.txt without deleted movie
    with open(MOVIE_FILE, "w") as f:
        for m in movies:
            f.write(f"{m['title']},{m['hall']},{m['start']},{m['end']}\n")

    print(f"\n'{removed['title']}' at Hall {removed['hall']} {removed['start']} deleted successfully!")


