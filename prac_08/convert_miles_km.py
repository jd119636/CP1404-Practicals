from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class ConvertToKilometers(App):
    """A Kivy app that converts miles to kilometres."""

    def build(self):
        """Set up the application window and load the KV layout."""
        Window.size = (400, 200)
        self.title = "Miles → Kilometres Converter"
        return Builder.load_file('convert_miles_km.kv')

    def handle_calculate(self):
        """Convert input miles to kilometres and update the result label."""
        miles = self.get_validated_miles()
        km = miles * MILES_TO_KM
        self.root.ids.output_label.text = f"{km:.2f}"

    def handle_increment(self, change):
        """
        Adjust the miles value by a given amount (up/down buttons),
        update the input, and recalculate the output.
        """
        miles = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def get_validated_miles(self):
        """
        Safely read the miles input and convert it to a float.
        Returns 0.0 if the input is invalid.
        """
        text = self.root.ids.input_miles.text
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertToKilometers().run()
