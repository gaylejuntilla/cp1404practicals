def main():
    filename = "wimbledon.csv"
    data = get_data(filename)


def get_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
        return data
