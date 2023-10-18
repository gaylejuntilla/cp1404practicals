

COLOUR_TO_CODE = {"absolutezero": "#0048ba", "acidgreen": "#b0bf1a", "aliceblue": "	#f0f8ff", "amaranth": "	#e52b50", "amber": "#ffbf00",
                  "amethyst": "#9966cc", "antiquewhite": "#faebd7", "apricot": "#fbceb1", "armygreen": "#4b5320", "asparagus": "#87a96b"}

colour_name = input("Colour name: ").lower()
while colour_name != "":
    try:
        print(f"The code for {colour_name} is {COLOUR_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Colour name: ").lower()
