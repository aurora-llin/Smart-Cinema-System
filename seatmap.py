import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ROWS = ['A', 'B', 'C', 'D', 'E', 'F']
COLS = [1, 2, 3, 4, 5, 6, 7, 8]

#open filename as f and add to seatmap as nested list( an inner list representing a row of seats)
def load_seatmap(hall):
    filename = os.path.join(BASE_DIR, f"layout_{hall}.txt")
    seatmap = []
    try:
        with open(filename, "r") as f:
            for line in f:
                seatmap.append(line.strip().split(","))
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return seatmap


def display_seatmap(seatmap):
    print("\n                 S C R E E N")
    print("  " + "-" * 40)
    print(format("1",">7s"), format("2",">3s"),format("3",">5s"),format("4",">3s"),format("5",">3s"),format("6",">3s"),format("7",">5s"),format("8",">3s"))

    for i, row in enumerate(seatmap):
        label = ROWS[i]
        seats = []
        for j, seat in enumerate(row):
            if seat == "O":
                display = "[ ]"
            else:
                display = "[X]"
            # Add aisle gap after column 2 and column 6
            if j == 2 or j == 6:
                seats.append("  " + display)
            else:
                seats.append(display)
        print(f"  {label}  " + " ".join(seats))

    print("  " + "-" * 40)
    print("  [ ] = Available    [X] = Occupied")

def is_seat_available(seatmap, row, col):
    return seatmap[row][col] == "O" 

def update_seat(seatmap, row, col, status):
    seatmap[row][col] = status  # "X" to booked, "O" to free

#overwrite the file by rejoining the updated seatmap list
def save_seatmap(seatmap, hall):
    filename = os.path.join(BASE_DIR, f"layout_{hall}.txt")
    with open(filename, "w") as f:
        for row in seatmap:
            f.write(",".join(row) + "\n")

def get_row_index(letter):
    return ROWS.index(letter.upper())

def get_col_index(number):
    return COLS.index(int(number))

# #test
# print(load_seatmap("A"))
#print(is_seat_available(load_seatmap("A"), get_row_index("A"), get_col_index(1)))
#print(update_seat(load_seatmap("A"), get_row_index("A"), get_col_index(1), "X"))


