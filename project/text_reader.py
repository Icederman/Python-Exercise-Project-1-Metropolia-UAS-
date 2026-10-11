from path_creator import path_creator

# Reads passed text file
def read_text(filename):
    path = path_creator(filename)
    try:
        with open(path, "r") as file:
            print(f"\n{file.read()}")
    except FileNotFoundError:
        print("intro File not found!")
