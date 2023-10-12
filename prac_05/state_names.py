"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

# state_code = input("Enter short state: ").upper()
# while state_code != "":
#     if state_code in CODE_TO_NAME:
#         print(state_code, "is", CODE_TO_NAME[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()

for state, state_name in CODE_TO_NAME.items():
    max_state_length = max(len(state) for state in CODE_TO_NAME.keys())
    max_sate_name_length = max(len(state_name) for state_name in CODE_TO_NAME.values())
    print(f"{state:{max_state_length}} is {state_name:{max_sate_name_length}}")
