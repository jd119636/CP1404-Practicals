# name = input("Hello: ")
# print("Hello", name)

# monthly_cost = float(input("Monthly cost: "))
# total_cost = monthly_cost * 12
# print(f"The total is ${total_cost:.2f}")


# age = int(input("Enter your age: "))
# while age < 0 or age > 150:
#     print("Invalid age")
#     age = int(input("Enter your age: "))
#
# if age >= 66:
#     category = ("old")
# elif age >= 18:
#     category = ("Adult")
# elif age >= 5:
#     category = ("Child")
# else:
#     category = ("Baby")
# print(f"Your age {age} is considered {category}")


# secret_number = 5
# input_number = int(input("Enter a number from 1 - 10: "))
# while input_number != secret_number:
#     print("Guess again ")
#     input_number = int(input("Enter a number from 1 - 10: "))
# print("You Win")

# for i in range(1, 5):
#     print (i)

# name = "Indra"
# for character in name:
#     print (character)
#

# def print_line(length):
#     print('-' * length)
#
# print_line(30)

# def print_grid(number_of_rows, number_of_columns):
#     for i in range(number_of_rows):
#         print("*"*number_of_columns)
#
# print_grid(3, 7)


# def get_limits():
#     low = int(input("enter lower limit: "))
#     high = int(input("enter upper limit: "))
#     return low, high, -1
# thing = get_limits()
# print(thing)
# print(type(thing))
#


# import random
# def print_secret_name(name):
#     letters = list(name)
#     random.shuffle(letters)
#     print("".join(letters))
#
# def display_menu():
#     print("\nMenu:")
#     print("G - get Valid Non Empty Name")
#     print("P - Hello")
#     print("S - Print Secret name")
#     print("Q - Quit")
#
# def get_name():
#     name = input("Enter your name: ")
#     while name == "":
#         print("Name cannot be blank")
#         name = input("Enter your name: ")
#     return name
#
# def print_line(length):
#     print("-" * length)
#
# def Print_greeting():
#     Length= (len(name)+6)
#     print_line(Length)
#     print(f"Hello {name}")
#     print_line(Length)
#
#
#
# display_menu()
# choice = input("\n Which option would you like to choose: ").upper()
#
#
#
# while choice != "Q":
#     if choice == "G":
#         name = get_name()
#         display_menu()
#         choice = input("Which option would you like to choose: ").upper()
#     elif choice == "P":
#         Print_greeting()
#         display_menu()
#         choice = input("Which option would you like to choose: ").upper()
#     elif choice == "S":
#         print_secret_name(name)
#         display_menu()
#         choice = input("Which option would you like to choose: ").upper()
#     else:
#         print("Invalid choice")
#         display_menu()
#         choice = input("Which option would you like to choose: ").upper()
# print("Thank you for playing")
#


# def print_line (length, pen = '-'):
#     print(pen*length)
#
# print_line(5)


# FILENAME = "secret.txt"
#
#
# def main():
#     secret = load_number(FILENAME)
#     guess = get_valid_number()
#     while guess != secret:
#         print("Guess again")
#         guess = get_valid_number()
#     print("you got it")
#
# def get_valid_number():
#     is_valid_input = False
#     while not is_valid_input:
#         try:
#             guess = int(input("Guess a number: "))
#             is_valid_input = True
#         except ValueError:
#             print("Invalid integer")
#     return guess
#
# get_valid_number()
#
# def load_number(filename):
#     try:
#         infile = open(filename, "r")
#         number = int(infile.read())
#     except ValueError:
#         print(f"Invalid number in {filename}")
#         number = 6
#     except FileNotFoundError:
#         print(f"File {filename} not found")
#         number = 4
#     else:
#         infile.close()
#     return number
#
# main()


# line = "Indra Kiiver...."
# line.strip('.')
# print (line.strip())

"""opens a file and reads"""
# from prac_05.wimbledon import in_file

# infile = open("SECRET.md")
# infile.readlines("#")
# infile.close()

# with open("data.txt", "r") as infile:
#     infile.readline()   #ignore header
#     for line in infile:
#         # print(line)
#         parts = line.strip().split(',')
#         # print(parts)
#
#         name = parts[0]
#         age = int(parts[1])
#         print(f"{name} will be {age+1} years old next year")

# infile = open("dataset.txt","r")
# for line in infile:
#     parts = line.strip("\n").split(',')
#     name = parts[0]
#     age = int(parts[1])
#     cost = float(parts[2]).strip("\n")
#     print(f"{name} was made in {age} and costs {cost}.")

# names = ("Craig", "Michael", "Terrance", "Philip")
# number = int(input(f"Enter number up to {len(names)}:"))
# try:
#     print(names[number-1])
# except IndexError:
#     print("Invalid input.")

# from operator import itemgetter
# data = [['Derek', 7], ['Carrie', 8],['Bob', 6], ['Aaron', 9] ]
# # data.sort()
# data.sort(key=itemgetter(1), reverse = True)
# for record in data:
#     print(data)

# score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]
# data = input ("Enter a name and score:")
# parts = data.split()
# score_pairs.append(parts)
# print(score_pairs)

"""stores the first and second term in the list"""
# fruit = ['orange', 'apple', 'pear', 'banana']
# balls = "-{}- {}".format(*fruit)
# print(balls)


"""Display income report for incomes over a given number of months."""
# def main():
#     incomes = []
#     months = int(input("How many months? "))
#
#     for month in range(1, months + 1):
#         income = float(input(f"Enter income for month: $"))
#         incomes.append(income)
#
#     print("\nIncome Report\n-------------")
#     total = 0
#     for month in range(1, months + 1):
#         income = incomes[month - 1]
#         total += income
#         print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
#
#
# main()


"""converts strings to integers"""
# almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# numbers = [int(number.strip()) for number in almost_numbers]
# print(numbers)

"""prints names longer than 11 characters"""
# long_names = [name for name in full_names if len(name) > 11]
# for name in long_names:
#     print(name)

"""Code does not generate duplicates through sample also join turns it into an integer"""
# import random
# quick_picks = int(input ("how many quick picks would you like to generate? :"))
# for i in range(quick_picks):
#     numbers = random.sample(range (1, 45), 6)
#     numbers.sort()
#     print(" ".join(f"{number:2}" for number in numbers))


"""asks if balls is a string"""
# from tkinter.font import names
# isinstance("balls", str)

"""finds the oldest in the list and prints the names if multiple people are the max age"""
# data_names = ['John', 'Bob', 'Joe', 'James']
# data_ages = [21, 34, 56, 56]
#
# def find_oldest(data_names, data_ages):
#     oldest_age = max(data_ages)
#
#     count = data_ages.count(oldest_age)
#     if count > 1:
#         print(f"The oldest age is {oldest_age}.")
#         print("People with that age:")
#         for i in range(len(data_ages)):
#             if data_ages[i] == oldest_age:
#                 print(f"- {data_names[i]}")
#     else:
#         index = data_ages.index(max(data_ages))
#         print(index)
#         print (f"{data_names[index]} is {max(data_ages)}")
#
# find_oldest(data_names, data_ages)


"""within a dictionary, removing witching names, adding names before"""
# name_to_age = {'Ben' : 10, 'Sam': 20, 'Xarah': 30}
# name_to_age ['Lucas'] = 40
# name_to_age ['Zara'] = name_to_age.pop('Xarah')
# print(name_to_age)
#


"""lists name and numbers of people for a dictionary"""
# name_to_age = {'Ben' : 10, 'Sam': 20, 'Xarah': 30}
# for name,age in name_to_age.items():
#     print(name,age)
#
# ages = list(name_to_age.values())
# ages.sort()
# print(ages)
# for name in name_to_age:
#     print(f"{name} is {name_to_age[name]} years old")

"""dictionary, new name and age and prints nicely"""
# name_to_age = {'Bill' : 21, 'Jane': 4, 'Sven': 56}
# new_name = str(input("enter your new name: "))
# new_age = int(input("enter your new age: "))
# name_to_age[new_name] = new_age
# max_length = max(len(new_name) for new_name in list(name_to_age.keys()))
# for name in name_to_age:
#     print(f"{name:{max_length}} is {name_to_age[name]:3} years old")

"""splits the text by commas, then join removes the quotes"""
# text = """EG2000 EG2008 EG2000 EG2008"""
# print(",".join(set(text.split())))

"""step out and open, strip all lines"""
# in_file = open('../data/wimbledon')
# lines = [line,strip() for line in in_file.readlines()]

"""using jason (accessing things in dictionary) and adding text to a dictionary"""
# import json
# demo_text = """{"number": 1, "title": "Demo", "state": "open"}"""
#
# thing = json.loads(demo_text)
# print(thing)
# print(type(thing))
# print(thing['title'])
# thing['title'] = thing['title'].upper()
# print(thing['title'])
#
# text = json.dumps(thing)
# print(text)
# print(type(text))

"""inputs emails until blank, then prints the name  followed by the email"""

# def split_email(email):
#     """Split an email into first and last name parts"""
#     name_part = email.split("@")[0]
#     split_name = name_part.split(".")
#     return split_name
#
#
# email_set = []
# email = input("Enter an email: ").lower()
#
# while email != "":
#     choice = input(f"is your email {email} Y/N:").lower()
#     if choice == "y":
#         split_name = split_email(email)
#         email_set.append([email, split_name])
#     elif choice == "n":
#         pass
#     else:
#         print("Please press Y or N")
#     email = input("Enter an email: ").lower()
#
# print("\nSaved email list:")
# for email, name_parts in email_set:
#     first_name = name_parts[0].capitalize()
#     last_name = name_parts[1].capitalize()
#     print(f"{first_name} {last_name} ({email})")

"""getting things from lists in lists"""
# on_sale_products = []
# products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
#
# for name, price, on_sale in products:
#     if on_sale:  # same as if on_sale == True
#         on_sale_products.append(name)
#
# print(on_sale_products)


"""Reading from a csv file """
# import csv
# reader = csv.reader(in_file)
# for row in reader:
#     print(row)
#

"""Skipping first line """
# in_file.readline()
"""turning a large number into a readable number for a csv """
# row[2] = int(row[2].replace(',', ''))

"""slicing off the last character"""
# row[3]=float(row[3][:-1])

"""Only keeping the last 4 characters"""
# row[3]=float(row[3][-4:])

"""Work with separate files"""
# class City:
#     def __init__(self, name = "", population = 0, percent = 0.0):
#         self.name = name
#         self.population = population
#         self.percent = percent
#
#     def __str__(self):
#         return f"{self.name}, {self.population: ,}, {self.percent}%"

"""Having a file called city  with"""
# from prac_06 import City
# city = City(row[1],row[2],row[3])

"""sees if the variable is something else"""
# isinstance(x, int)

"""method to add special values"""
# def __add__ (self, other):
#     return City(self.name + other.name)

"""class work"""
# def __eq__ (self, other):
#     return City(self.name == other.name, self.age == other.age)

"""to link something"""
# [me](https:)

"""datetime module"""
# import datetime
# balls = datetime.date(2022, 11, 23)
# print (balls.strftime("%d %b %Y (%A)"))
