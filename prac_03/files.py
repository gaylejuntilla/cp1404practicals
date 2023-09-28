out_file = open("name.txt", 'w')
name = input("Name: ")
print(name, file=out_file)
out_file.close()

FILENAME = "name.txt"
in_file = open(FILENAME, 'r')
name = in_file.read()
in_file.close()
print(f"Your name is {name}")
