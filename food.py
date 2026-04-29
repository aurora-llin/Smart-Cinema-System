import datetime

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def display_menu():
    print("\n" + "╔" + "═"*38 + "╗")
    print("║        FOOD COURT                    ║")
    print("╚" + "═"*38 + "╝")
    print(" POPCORN BUCKETS:")
    print(" • Medium: $5.50 | Large: $6.50")
    print(" • Flavors: Sweet, Caramel, Salty, Cheese, Seaweed, Cheetos")
    print("\n DRINKS:")
    print(" • Coke: Small: $1.00, Medium: $2.00, Large: $2.75")
    print(" • Water: $1.00")
    print("\n SNACKS:")
    print(" • Chicken Nuggets: $2.50 | Fries: $1.75")
    print(" • Hot Dog: $1.00 | Dry Noodles Set: $3.25")
    print("\n COMBOS (BEST VALUE):")
    print(" [1] Couple Set: 1 Large Popcorn + 2 Medium Drinks -> $6.00")
    print(" [2] Single Set: 1 Medium Popcorn + 1 Large Drink  -> $5.00")
    print(" [3] Party Set:  2 Large Popcorn + 4 Large Drinks + Nuggets -> $20.00")
    print("═"*50)

def save_to_file(cart, total):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("orders.txt", "a") as f:
        f.write(f"\n--- ORDER DATE: {timestamp} ---\n")
        for item in cart:
            f.write(f"- {item}\n")
        f.write(f"FINAL TOTAL: ${total:.2f}\n")
        f.write("-" * 30 + "\n")

def order_food():
    cart = []
    total_cost = 0.0
    flavors_list = ["Sweet", "Caramel", "Salty", "Cheese", "Seaweed", "Cheetos"]

    while True:
        print("\n WHAT WOULD YOU LIKE TO DO?")
        print(" ---------------------------")
        print(" • [1] Add Popcorn")
        print(" • [2] Add Drinks")
        print(" • [3] Add Snacks")
        print(" • [4] Add Combos")
        print(" • [5] View Cart")
        print(" • [6] Checkout & Save")
        
        choice = input("\nSelect an option (1-6): ")

        if choice == '1':
            size = input("Select Size (M/L): ").upper()
            price = 5.50 if size == 'M' else 6.50
            print(f"Available: {', '.join(flavors_list)}")
            f_choice = input("Pick up to 2 flavors (comma separated): ").split(",")
            f_clean = [f.strip() for f in f_choice][:2]#make sure only two flavors are added
            cart.append(f"{size} Popcorn ({', '.join(f_clean)}) - ${price:.2f}")
            total_cost += price

        elif choice == '2':
            print(" 1. Coke(S) $1.00 | 2. Coke(M) $2.00 | 3. Coke(L) $2.75 | 4. Water $1.00")
            d_choice = input("Select drink: ")
            if d_choice == '1': cart.append("Small Coke - $1.00"); total_cost += 1.00
            elif d_choice == '2': cart.append("Medium Coke - $2.00"); total_cost += 2.00
            elif d_choice == '3': cart.append("Large Coke - $2.75"); total_cost += 2.75
            elif d_choice == '4': cart.append("Water - $1.00"); total_cost += 1.00

        elif choice == '3':
            print(" 1. Nuggets $2.50 | 2. Fries $1.75 | 3. Hot Dog $1.00 | 4. Noodles Set $3.25")
            s_choice = input("Select snack: ")
            if s_choice == '1': cart.append("Nuggets - $2.50"); total_cost += 2.50
            elif s_choice == '2': cart.append("Fries - $1.75"); total_cost += 1.75
            elif s_choice == '3': cart.append("Hot Dog - $1.00"); total_cost += 1.00
            elif s_choice == '4': cart.append("Noodles Set - $3.25"); total_cost += 3.25

        elif choice == '4':
            print(" 1. Couple Set ($6.00) | 2. Single Set ($5.00) | 3. Party Set ($20.00)")
            c_choice = input("Select combo: ")
            if c_choice == '1': cart.append("Couple Set - $6.00"); total_cost += 6.00
            elif c_choice == '2': cart.append("Single Set - $5.00"); total_cost += 5.00
            elif c_choice == '3': cart.append("Party Set - $20.00"); total_cost += 20.00

        elif choice == '5':
            print("\n YOUR CURRENT CART:")
            if not cart:
                print("   (Empty)")
            else:
                for item in cart:
                    print(f"   • {item}")
                print(f"   SUBTOTAL: ${total_cost:.2f}")

        elif choice == '6':
            if not cart:
                print("\n Cannot checkout with an empty cart!")
                continue
            
            save_to_file(cart, total_cost)
            print("\n--- FINAL RECEIPT ---")
            for item in cart:
                print(f"- {item}")
            print(f"TOTAL AMOUNT: ${total_cost:.2f}")
            print("----------------------\nThank you for purchasing, please enjoy your movie!")
            
            return cart, total_cost 
            
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__": #same as main function in java, this will only run if this file is executed directly, not imported as a module
    display_menu()
    order_food()


