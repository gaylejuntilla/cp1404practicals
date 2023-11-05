"""
Project Management Program
Estimated Time: Too long (longer than the amount of time I have to complete this (1.5hrs)
Actual Time:
"""

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project" \
       "\n(U)pdate project\n(Q)uit"


def main():
    print(MENU)
    choice = input(">>> ")
    while choice != "Q":
        if choice =="L":
            filename = input("filename: ")
            projects = load_projects(filename)


def load_projects(filename):
    projects = []
    with open(filename, "r") as in_file:
        for line in in_file:




main()
