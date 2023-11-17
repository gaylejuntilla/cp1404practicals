from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """"""
    def __init__(self, fanciness: float, **kwargs):
        """"""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

