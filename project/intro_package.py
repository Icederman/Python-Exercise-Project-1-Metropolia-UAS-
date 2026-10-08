import os

# Reads the intro text
# With .join and .abspath, python removes the internal folders and combines it into a single directory.
def show_intro(filename):
    path = os.path.abspath(os.path.join(__file__,"..","..",filename))
    try:
        with open(path, "r") as file:
            print(f"\n{file.read()}")
    except FileNotFoundError:
        print("intro File not found!")

# Reads the rules text
# Same as the intro text method usage
def show_rules(filename):
    path = os.path.abspath(os.path.join(__file__,"..","..",filename))
    try:
        with open(path, "r") as file:
            print(f"\n{file.read()}")
    except FileNotFoundError:
        print("rules File not found!")