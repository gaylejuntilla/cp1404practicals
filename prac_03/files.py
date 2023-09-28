# out_file = open("name.txt", 'w')
# name = input("Name: ")
# print(name, file=out_file)
# out_file.close()
#
# FILENAME = "name.txt"
# in_file = open(FILENAME, 'r')
# name = in_file.read()
# in_file.close()
# print(f"Your name is {name}")

# in_file = open("numbers.txt", "r")
# number1 = int(in_file.readline())
# number2 = int(in_file.readline())
# in_file.close()
# print(number1 + number2)

in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)

