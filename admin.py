
import movie
import seatmap

def display_admin_menu():
    print("========================================")
    print("           ADMIN DASHBOARD              ")
    print("========================================")
    print("---- Movies ----")
    print("1. View All Movies")
    print("2. Add a Movie")
    print("3. Delete a Movie")
    print("---- Seats ----")
    print("4. View Seats for a Movie")
    print("5. Back")
    print("----------------------------------------")

def admin_flow():
    while True:
        display_admin_menu()
        choice = input("Please select an option (1-5): ")

        if choice == '1':
            movies = movie.load_movies()
            movie.display_movies(movies)
        elif choice == '2':
            movie.add_movie()
        elif choice == '3':
            movie.delete_movie()
        elif choice == '4':
            view_seats()
        elif choice == '5':
            print("Logging out of admin panel...")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")

        input("\nPress Enter to continue...")

def view_seats():
    movies = movie.load_movies()
    movie.display_movies(movies)

    while True:
        try:
            choice = int(input("\nSelect a movie number to view seats: "))
            if 1 <= choice <= len(movies):
                selected = movies[choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(movies)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\n{selected['title']} | Hall {selected['hall']} | {selected['start']} - {selected['end']}")
    seatmap_data = seatmap.load_seatmap(selected['hall'], selected['start'])
    seatmap.display_seatmap(seatmap_data)