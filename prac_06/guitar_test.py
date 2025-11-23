"""Start time: 11:31
Estimated time: 30 mins
end time:12:47"""

from prac_06.guitar import Guitar


def main():
    """adds a new guitar to the guitars list, then displays details and if its vintage"""
    guitars = []
    print("Add details for a new guitar:")
    name = str(input(f"input a name:"))
    while name != '':
        year = int(input(f"input a year:"))
        cost = float(input(f"input a cost:"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} has been added to the guitars list.")
        name = str(input(f"input a name:"))

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print(f"these are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "Vintage"
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
    else:
        print("No guitars, go buy one")


main()


