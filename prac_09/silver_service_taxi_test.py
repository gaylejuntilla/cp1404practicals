from silver_service_taxi import SilverServiceTaxi


taxi = SilverServiceTaxi(name="Fancy Taxi", fuel=50, fanciness=2)
taxi.drive(18)
print(taxi)
print(taxi.get_fare())

# taxi = SilverServiceTaxi(name="Limo", fuel=100, fanciness=2)
# taxi.drive(59)
# print(taxi.get_fare())