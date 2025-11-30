from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness-based price increase."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        base_price = Taxi.price_per_km
        self.price_per_km = base_price * fanciness

    def __str__(self):
        return f"{super().__str__()}, plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        return super().get_fare() + self.flagfall
