from silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi(name="Fancy Taxi", fuel=50, fanciness=2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
