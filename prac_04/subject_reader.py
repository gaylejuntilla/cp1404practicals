"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print("----------")
        print(parts)  # See if that worked
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    for subject_detail in data:
        subject = subject_detail[0]
        teacher = subject_detail[1]
        number_of_students = subject_detail[2]
        # print("{} is taught by {} and has {} students". format(*subject_detail))
        print(f"{subject} is taught by {teacher:12} and has {number_of_students:3}")


main()
