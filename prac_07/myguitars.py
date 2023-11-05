from guitar import Guitar


def main():
    guitars = []
    with open("guitars.csv", "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            parts[1] = int(parts[1])
            parts[2] = float(parts[2])
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)
            print(guitar)
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        print(f"{new_guitar} added")
        guitars.append(new_guitar)
        name = input("Name: ")
    guitars.sort()
    with open("guitars.csv", "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
