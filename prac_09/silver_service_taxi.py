from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """"""
    flagfall = 4.50

    def __init__(self, fanciness: float, **kwargs):
        """"""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
