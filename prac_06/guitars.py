"""
Playing the Guitars
Estimated time: 1hr
Actual time: 35 minutes
"""

from guitar import Guitar


def main():
    print("My guitars!")
    name = input("Name: ")
    guitars = []
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        print(f"{new_guitar} added")
        guitars.append(new_guitar)
        name = input("Name: ")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"{i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:,.2f} {vintage_string}")


main()
