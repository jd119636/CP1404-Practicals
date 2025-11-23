# data = []
# for numbers in range (1, 6):
#     number_set = float(input("please enter 5 numbers:"))
#     data.append(float(number_set))
# print(f"the first number is {data[0]}")
# print(f"the last number is {data[-1]}")
# print(f" the smallest number is {min(data)}")
# print(f" the largest number is {max(data)}")
# print(f" the average number is {sum(data)/len(data)}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
data = []
name = input ("Input a valid username:")
data.append(name)
while name not in usernames:
    print("you may not proceed")
    name = input ("Input a valid username:")
else:
    print("you are in")
