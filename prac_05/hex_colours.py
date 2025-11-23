colour_set = {"Absolute Zero": "#0048ba", "Acid Green": "	#b0bf1a", "Alice Blue": "	#f0f8ff", "Alizarin crimson": "	#e32636", "Amaranth": "	#e52b50", "Amber": "	#ffbf00", "Amethyst": "	#9966cc", "Antique White": "	#faebd7", "Apricot": "#fbceb1", "Aqua": "#00ffff"}
lower_colour_set = {name.lower(): code for name, code in colour_set.items()}
print(lower_colour_set)
colour = input("Enter a colour: ").lower()
while colour != "":
    try:
        print(f"{colour}, is, {lower_colour_set[colour]}")
        colour = input("Enter a colour: ").lower()
    except KeyError:
        print("Invalid colour")
        colour = input("Enter a colour: ").lower()