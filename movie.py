def load_movies():
    movies = []
    try:
        with open("movies.txt", "r") as f:
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

#test
display_movies(load_movies())
