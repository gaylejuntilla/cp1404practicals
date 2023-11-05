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
    guitars.sort()
    print(guitars)


main()
