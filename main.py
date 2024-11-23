import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the file
file_path = os.path.join(script_dir, 'books', 'frankenstein.txt')

# Open and read the file
try:
    with open(file_path, 'r') as file:
        text = file.read()

    # Count the words in the text
    words = text.split()
    word_count = len(words)
    
    # Count the number of times each character appears
    char_count = {}
    for char in text.lower():
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    # Sort the character counts in descending order
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    # Print the report
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

except FileNotFoundError:
    print(f"The file {file_path} does not exist.")