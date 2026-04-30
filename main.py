import booking
def display_main_menu():
    print("========================================")
    print("                OPTIMA                  ")
    print("      SMART CINEMA BOOKING SYSTEM       ")
    print("========================================")
    print("1. Book Tickets")
    print("2. View My Bookings")
    print("3. Cancel a Booking")
    print("4. Save & Exit")
    print("----------------------------------------")


while True:
    display_main_menu()
    menu_choice = input("Please select an option (1-4): ")
    if menu_choice == '1':
        booking.book_tickets()
    elif menu_choice == '2':
        booking.view_bookings()
    elif menu_choice == '3':
        booking.cancel_booking()
    elif menu_choice == '4':
        print("Thank you for using Smart Cinema Booking system. Goodbye!")
        break
    else:
        print("Invalid option. Please enter a number between 1 and 4.")

    input("\nPress Enter to return to the main menu...")