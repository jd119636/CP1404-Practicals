

from prac_09.unreliable_car import UnreliableCar

def main():
    """tests the reliability of 2 cars by running through a loop"""
    bad_car = UnreliableCar("Dodge", 100, 20)

    good_car = UnreliableCar("Toyota", 100, 90)

    print("Testing unreliable cars...\n")

    for i in range(10):
        distance = 10
        print(f"Attempt {i+1}:")
        print(f"Good car attempted to drive {distance}km and drove:",
              good_car.drive(distance))
        print(f"Bad car attempted to drive {distance}km and drove:",
              bad_car.drive(distance))
        print()

if __name__ == "__main__":
    main()
