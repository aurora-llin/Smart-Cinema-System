import booking
import admin
ADMIN_PASSWORD = "admin123" #Admin shares the same password for simplicity for now
def display_role_menu():
    print("========================================")
    print("      SMART CINEMA BOOKING SYSTEM       ")
    print("========================================")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    print("----------------------------------------")

def display_main_menu():
    print("========================================")
    print("           CUSTOMER MENU                ")
    print("========================================")
    print("1. Book Tickets")
    print("2. View My Bookings")
    print("3. Cancel a Booking")
    print("4. Get Invoice")   #new
    print("5. Back")
    print("----------------------------------------")

def user_flow():
    while True:
        display_main_menu()
        menu_choice = input("Please select an option (1-5): ")

        if menu_choice == '1':
            booking.book_tickets()
        elif menu_choice == '2':
            booking.view_bookings()
        elif menu_choice == '3':
            booking.cancel_booking()
        elif menu_choice == '4':
            bid = input("Enter booking ID: ").strip().upper()
            booking.get_invoice(bid)
        elif menu_choice == '5':
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")

        input("\nPress Enter to continue...")
while True:
    display_role_menu()
    role = input("Please select who you are (1-3): ")

    if role == '1':
        user_flow()
    elif role == '2':
        password = input("Enter admin password: ")
        if password == ADMIN_PASSWORD:
            print("Access granted! Welcome, Admin.")
            admin.admin_flow()
        else:
            print("Incorrect password. Access denied.")
            input("\nPress Enter to continue...")
    elif role == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please enter 1, 2, or 3.")