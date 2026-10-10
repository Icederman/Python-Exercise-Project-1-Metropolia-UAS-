from pathcreator_package import path_creator

# Reads the intro text
def show_intro(filename):
    path = path_creator(filename)
    try:
        with open(path, "r") as file:
            print(f"\n{file.read()}")
    except FileNotFoundError:
        print("intro File not found!")

# Reads the rules text
# Same as the intro text method usage
def show_rules(filename):
    path = path_creator(filename)
    try:
        with open(path, "r") as file:
            print(f"\n{file.read()}")
    except FileNotFoundError:
        print("rules File not found!")