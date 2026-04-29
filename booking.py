import movie
import seatmap
import smartPricing
import food
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOKINGS_FILE = os.path.join(BASE_DIR, "bookings.txt")

def generate_booking_id(): #initially I used random numbers but then I thought about possible diplicates.
    try:
        with open(BOOKINGS_FILE, "r") as f:
            lines = f.readlines()
            count = len(lines) + 1  
    except FileNotFoundError:
        count = 1
    return f"BK{count:04d}"

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
    showtime = selected_movie['start']
    seatmap_data = seatmap.load_seatmap(hall,showtime)
    seats = []
    row_inputs = [] #we are using that in row based pricing later in pricing section
    while True:
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
                seats.append(f"{row_input}{col_input}")
                row_inputs.append(row_input)  # for pricing later
                seatmap.update_seat(seatmap_data, row_index, col_index, "X")  
                print(f"Seat {row_input}{col_input} added!")
                break
            else:
                print(f"Seat {row_input}{col_input} is already occupied. Please choose another.")
        another = input("Add another seat? (yes/no): ").lower()
        if another != 'yes':
                break
    seat_record = " & ".join(seats)
    print(f"\nSeats confirmed: {seat_record}")


    # Step 3: Food pre-order 
    print("\n--- Food Pre-order ---")
    want_food = input("Would you like to pre-order food? (yes/no): ").lower()
    if want_food == 'yes':
        food.display_menu()
        food_cart, food_cost = food.order_food()
        food_order = " | ".join(food_cart)  # saves as one string to bookings.txt
    else:
        food_cart = []
        food_cost = 0.00
        food_order = "None"

    # Step 4: Pricing
    print("\n--- Pricing ---")
    ticket_price = sum(smartPricing.get_seat_price(r) for r in row_inputs)
    discount_code = input("Enter discount code (or press Enter to skip): ")
    if discount_code:
        discount = smartPricing.apply_discount(ticket_price, discount_code)
        print(f"Discount applied: -${discount:.2f}")
    else:
        discount = 0.00
        print("No discount code entered.")

    total = ticket_price + food_cost - discount
    print(f"\nTicket Price : ${ticket_price:.2f}")
    print(f"Food Cost    : ${food_cost:.2f}")
    print(f"Discount     : -${discount:.2f}")
    print(f"Total        : ${total:.2f}")

    # Step 5: Confirm booking
    confirm = input("\nConfirm booking? (yes/no): ").lower()
    if confirm != 'yes':
        print("Booking cancelled.")
        return

    # Step 6: Save booking
    name = input("Enter your name: ")
    booking_id = generate_booking_id()

    seatmap.save_seatmap(seatmap_data, hall,showtime)  # save updated seatmap with booked seats

    # save showtime in booking record
    booking_record = f"{booking_id},{name},{selected_movie['title']},Hall {hall},{selected_movie['start']},{seat_record},{food_order},{total:.2f}\n"
    print(f"\n Booking confirmed! Your booking ID is: {booking_id}")
    save_bookings(booking_record)

def save_bookings(booking_record):
    with open(BOOKINGS_FILE, "a") as f:
        f.write(booking_record)

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
                seat_field = parts[4]           # seats are stored with & seperated and as string
                seat_list = seat_field.split(" & ")  # split into a list for counting
                print(f"ID      : {parts[0]}")
                print(f"Name    : {parts[1]}")
                print(f"Movie   : {parts[2]}")
                print(f"Hall    : {parts[3]}")
                print(f"Seats   : {seat_field} ({len(seat_list)} seat(s))")
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
    hall = found[3].replace("Hall ", "")     # extract hall number from "Hall X"           
    seat_field = found[5]
    seat_list = seat_field.split(" & ")
    showtime = found[4]  # Get the showtime from the booking record
    seatmap_data = seatmap.load_seatmap(hall, showtime)
    for seat in seat_list:
        row_letter = seat[0]                           
        col_number = seat[1]                          
        row_index = seatmap.get_row_index(row_letter)
        col_index = seatmap.get_col_index(col_number)
        seatmap.update_seat(seatmap_data, row_index, col_index, "O")
        seatmap.save_seatmap(seatmap_data, hall, showtime)  

    # Remove booking from file
    with open(BOOKINGS_FILE, "w") as f:
        f.writelines(remaining)

    print(f"\nBooking {booking_id} has been cancelled and seats {seat_field} are now available.")

