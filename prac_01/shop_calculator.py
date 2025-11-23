total_cost = 0
number_of_items= int(input("Enter the number of items: "))

while number_of_items < 0:
    print("invalid number of items!")
    number_of_items = int(input("Enter the number of items: "))
for i in range(number_of_items):
    item_cost = float(input("Enter the cost of item: $ "))
    total_cost = total_cost + item_cost
if total_cost >100:
    total_cost = total_cost*0.9

print(f"number of items: {number_of_items}")
print(f"total cost of {number_of_items} items is :${total_cost: .2f}")