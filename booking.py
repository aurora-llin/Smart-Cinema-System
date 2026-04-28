import movie
import seatmap

BOOKINGS_FILE = "bookings.txt"

def book_tickets():
    # Step 1: Display and select movie
    movies = movie.load_movies()
    movie.display_movies(movies)

    while True:
        try:
            choice = int(input("\nSelect a movie number: "))
            if 1 <= choice <= len(movies):
                selected_movie = movies[choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(movies)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nYou selected: {selected_movie['title']} | Hall {selected_movie['hall']} | {selected_movie['start']} - {selected_movie['end']}")

    # Step 2: Display and select seat
    hall = selected_movie['hall']
    seatmap_data = seatmap.load_seatmap(hall)
    seatmap.display_seatmap(seatmap_data)

    while True:
        row_input = input("\nEnter row (A-F): ").upper()
        col_input = input("Enter column (1-8): ")

        if row_input not in ['A', 'B', 'C', 'D', 'E', 'F']:
            print("Invalid row. Please enter A to F.")
            continue
        if not col_input.isdigit() or not (1 <= int(col_input) <= 8):
            print("Invalid column. Please enter 1 to 8.")
            continue

        row_index = seatmap.get_row_index(row_input)
        col_index = seatmap.get_col_index(col_input)

        if seatmap.is_seat_available(seatmap_data, row_index, col_index):
            break
        else:
            print(f"Seat {row_input}{col_input} is already occupied. Please choose another.")

    # Step 3: Food pre-order (dummy for now)
    print("\n--- Food Pre-order ---")
    print("(Food system coming soon)")
    food_order = "None"
    food_cost = 0.00

    # Step 4: Pricing (dummy for now)
    print("\n--- Pricing ---")
    base_price = selected_movie['price']
    discount = 0.00
    total = base_price + food_cost - discount
    print(f"Base ticket price : ${base_price:.2f}")
    print(f"Food cost         : ${food_cost:.2f}")
    print(f"Discount          : -${discount:.2f}")
    print(f"Total             : ${total:.2f}")

    # Step 5: Confirm booking
    confirm = input("\nConfirm booking? (yes/no): ").lower()
    if confirm != 'yes':
        print("Booking cancelled.")
        return

    # Step 6: Save booking
    name = input("Enter your name: ")
    booking_id = generate_booking_id()

    seatmap.update_seat(seatmap_data, row_index, col_index, "X")
    seatmap.save_seatmap(seatmap_data, hall)

    booking_record = f"{booking_id},{name},{selected_movie['title']},Hall {hall},{row_input}{col_input},{food_order},{total:.2f}\n"
    save_bookings(booking_record)

    print(f"\n Booking confirmed! Your booking ID is: {booking_id}")


def view_bookings():
    print("\n========================================")
    print("           MY BOOKINGS")
    print("========================================")
    try:
        with open(BOOKINGS_FILE, "r") as f:
            lines = f.readlines()
            if not lines:
                print("No bookings found.")
                return
            for line in lines:
                parts = line.strip().split(",")
                print(f"ID      : {parts[0]}")
                print(f"Name    : {parts[1]}")
                print(f"Movie   : {parts[2]}")
                print(f"Hall    : {parts[3]}")
                print(f"Seat    : {parts[4]}")
                print(f"Food    : {parts[5]}")
                print(f"Total   : ${parts[6]}")
                print("----------------------------------------")
    except FileNotFoundError:
        print("No bookings found.")


def cancel_booking():
    booking_id = input("\nEnter your booking ID to cancel: ").strip()

    try:
        with open(BOOKINGS_FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No bookings found.")
        return

    found = None
    remaining = []

    for line in lines:
        parts = line.strip().split(",")
        if parts[0] == booking_id:
            found = parts
        else:
            remaining.append(line)

    if not found:
        print(f"Booking ID '{booking_id}' not found.")
        return

    # Free the seat
    hall = found[3].replace("Hall ", "")
    seat = found[4]                      # e.g. "B3"
    row_letter = seat[0]                 # "B"
    col_number = seat[1]                 # "3"

    seatmap_data = seatmap.load_seatmap(hall)
    row_index = seatmap.get_row_index(row_letter)
    col_index = seatmap.get_col_index(col_number)
    seatmap.update_seat(seatmap_data, row_index, col_index, "O")
    seatmap.save_seatmap(seatmap_data, hall)

    # Remove booking from file
    with open(BOOKINGS_FILE, "w") as f:
        f.writelines(remaining)

    print(f"\nBooking {booking_id} has been cancelled and seat {seat} is now available.")


def save_bookings(booking_record):
    with open(BOOKINGS_FILE, "a") as f:
        f.write(booking_record)


def generate_booking_id():
    import random
    return "BK" + str(random.randint(10000, 99999))