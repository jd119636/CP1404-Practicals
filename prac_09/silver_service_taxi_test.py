from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Create a SilverServiceTaxi with fanciness 2 and drive it 18km"""
    taxi = SilverServiceTaxi("Test Taxi", 100, 2)

    # Drive 18 km
    taxi.drive(18)

    # Calculate fare
    fare = taxi.get_fare()

    # Print info
    print(f"Trip fare: ${fare:.2f}")

    assert abs(fare - 48.78) < 0.1, f"Expected fare 48.78 but got {fare:.2f}"

    print("Test passed!")


if __name__ == "__main__":
    main()


