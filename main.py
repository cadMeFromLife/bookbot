import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the file
file_path = os.path.join(script_dir, 'books', 'frankenstein.txt')

# Open and read the file
try:
    with open(file_path, 'r') as file:
        text = file.read()
        print(text)
except FileNotFoundError:
    print(f"File not found: {file_path}")