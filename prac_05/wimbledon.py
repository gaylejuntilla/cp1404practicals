CHAMPION_INDEX = 2
COUNTRY_INDEX = 1


def main():
    """Process wimbledon.csv and display champions and countries"""
    filename = "wimbledon.csv"
    data = get_data(filename)
    champion_to_wins, countries = process_data(data)
    display_results(champion_to_wins, countries)


def display_results(champion_to_wins, countries):
    """Display champions, wins and countries"""
    print("Wimbledon Champions: ")
    for champion, wins in champion_to_wins.items():
        print(champion, wins, sep=" ")
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def process_data(data):
    """Create champion and wins dictionary and a set of winning countries"""
    champion_to_wins = {}
    countries = set()
    for record in data:
        try:
            countries.add(record[COUNTRY_INDEX])
            champion_to_wins[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_wins[record[CHAMPION_INDEX]] = 1
    return champion_to_wins, countries


def get_data(filename):
    """Open file and create nested list of data records"""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
        return data


main()
