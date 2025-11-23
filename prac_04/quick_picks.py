import random

quick_picks = int(input ("how many quick picks would you like to generate? :"))
for i in range(quick_picks):
    numbers = random.sample(range (1, 45), 6)
    numbers.sort()
    print(" ".join(f"{number:2}" for number in numbers))
