import csv

from prac_07.guitar import Guitar

guitar_list = []


def main():
    """Read guitars from CSV, allow user to add new ones, save to file."""

    # --- Step 1: Read existing guitars ---
    with open('guitars.csv', 'r') as in_file:
        next(in_file)  # skip header
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitar_list.append(guitar)

    # --- Step 2: Get new guitars from user ---
    print("Add details for a new guitar:")
    name = input("Input a name: ")

    while name != '':
        year = int(input("Input a year: "))
        cost = float(input("Input a cost: "))
        new_guitar = Guitar(name, year, cost)

        guitar_list.append(new_guitar)
        print(f"{new_guitar} has been added to the guitars list.")

        name = input("Input a name: ")

    # --- Step 3: Sort list (optional) ---
    guitar_list.sort()

    # --- Step 4: Write the updated list back to the CSV file ---
    with open('guitars.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Name", "Year", "Cost"])  # header

        for guitar in guitar_list:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

    # --- Step 5: Display all guitars ---
    print("\nUpdated guitar list:")
    for guitar in guitar_list:
        print(guitar)


main()
