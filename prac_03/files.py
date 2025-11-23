# name = input("Enter your name: ")
# FILENAME = ("name.txt")
# with open(FILENAME, "w") as file:
#     file.write(name)
#
# with open(FILENAME, "r") as file:
#     name = file.read()
#     print(name)

# FILENAME = ("numbers.txt")
# with open(FILENAME, "r") as file:
#     lines = file.readlines()[:-1]
#     num1 = int(lines[0].strip())
#     num2 = int(lines[1].strip())
#     sum = num1 + num2
#     print(sum)

FILENAME = ("numbers.txt")
with open(FILENAME, "r") as file:
    lines = file.readlines()
    num1 = int(lines[0].strip())
    num2 = int(lines[1].strip())
    num3 = int(lines[2].strip())
    sum = num1 + num2 + num3
    print(sum)
