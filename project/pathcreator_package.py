import os

# With .join and .abspath, python removes the internal folders and combines it into a single directory.
def path_creator(filename):
    return os.path.abspath(os.path.join(__file__,"..","..",filename))