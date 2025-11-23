def display_menu():
    print("G - Get a valid score")
    print("P - Print result")
    print("S - Show stars")
    print("Q - Quit")

def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def print_line(length):
    print("*" * length)

def print_stars(score):
    Length= (score)
    print_line(int(Length))

display_menu()
choice = input("Enter your choice: ").upper()
while choice != "Q":
    if choice == "G":
       score = get_valid_score()
       display_menu()
       choice = input("Enter your choice: ").upper()
    elif choice == "P":
        print(f"your score is {score}")
        display_menu()
        choice = input("Which option would you like to choose: ").upper()
    elif choice == "S":
        print_stars(score)
        display_menu()
        choice = input("Which option would you like to choose: ").upper()
    else:
        print("Invalid choice")
        choice = input("Which option would you like to choose: ").upper()
print("Thank you for playing")
