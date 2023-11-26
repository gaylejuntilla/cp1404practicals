from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver Service Taxi class"""
    flagfall = 4.50

    def __init__(self, fanciness: float, **kwargs):
        """Initialise a Silver Service Taxi object"""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Get taxi fare"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of taxi details including flagfall"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
