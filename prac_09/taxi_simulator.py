from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Simulate a taxi service tracker using Taxi and SilverServiceTaxi classes"""
    taxis = [Taxi(name="Prius", fuel=100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             # SilverServiceTaxi class uses key word arguments
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    current_taxi = None
    total_bill = 0
    print("Lets drive")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxi_options(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "d":
            if current_taxi:
                drive_distance = int(input("Drive how far? "))  # error checking?
                current_taxi.start_fare()
                current_taxi.drive(drive_distance)
                cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                total_bill += cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date is ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill}")
    print("Taxis are now:")
    display_taxi_options(taxis)


def display_taxi_options(taxis):
    """Display numbered taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
