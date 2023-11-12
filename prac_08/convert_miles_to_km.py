"""
Convert miles to km program
"""
from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM_RATIO = 1.609344


class MilesToKilometers(App):
    """ """

    def build(self):
        """ """
        self.title = "Convert miles to kilometers"
        self.root = Builder.load_file("convert_miles_to_km.kv")
        return self.root

    def get_miles(self):
        number_of_miles = float(self.root.ids.input_number.text)
        return number_of_miles

    def calculate_conversion(self):
        number_of_miles = self.get_miles()
        number_of_kilometers = number_of_miles * MILES_TO_KM_RATIO
        self.root.ids.output_label.text = str(number_of_kilometers)


MilesToKilometers().run()
