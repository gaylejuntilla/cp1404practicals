"""
Convert miles to km program
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_RATIO = 1.609344


class MilesToKilometers(App):
    """MilesToKilometers is an app that converts miles into kilometers"""
    number = StringProperty()

    def build(self):
        """Build app from the kv file"""
        self.title = "Convert miles to kilometers"
        self.root = Builder.load_file("convert_miles_to_km.kv")
        return self.root

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view"""
        self.number = self.root.ids.input_number.text

    def get_miles(self):
        """Get text input and convert into a float with error checking"""
        try:
            number_of_miles = float(self.root.ids.input_number.text)
            return number_of_miles
        except ValueError:
            return 0.0

    def calculate_conversion(self):
        """Convert float for number of miles into kilometers"""
        number_of_miles = self.get_miles()
        number_of_kilometers = number_of_miles * MILES_TO_KM_RATIO
        self.root.ids.output_label.text = str(number_of_kilometers)

    def handle_increment(self, increment_value):
        """Change the number of miles by +-1 to handle Up/Down button press"""
        number_of_miles = self.get_miles() + increment_value
        self.root.ids.input_number.text = str(number_of_miles)


MilesToKilometers().run()
