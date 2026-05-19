# Challenge 1: Multiples Generator
# Instructions:
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples:
# - number: 7, length: 5 -> [7, 14, 21, 28, 35]
# - number: 12, length: 10 -> [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
try:
    num_input = input("Enter the number: ")
    len_input = input("Enter the length: ")
    
    number = int(num_input)
    length = int(len_input)
    
    if length < 0:
        print("Error: Length must be a non-negative integer.")
    else:
        # Generate the list of multiples using a list comprehension
        multiples = [number * i for i in range(1, length + 1)]
        print(f"Multiples of {number} with length {length}: {multiples}")
except ValueError:
    print("Error: Please enter valid integers for both number and length.")





# Challenge 2: Remove Consecutive Duplicates
# Instructions:
# Write a program that asks a string to the user,
# and displays a new string with any duplicate consecutive letters removed.
# Examples:
# - "ppoeemm" -> "poem"
# - "wiiiinnnnd" -> "wind"
# - "ttiiitllleeee" -> "title"
# - "cccccaaarrrbbonnnnn" -> "carbon"
user_word = input("Enter a word: ").strip()
if not user_word:
    print("Error: Word cannot be empty.")
else:
    # Build a new string list by keeping only characters that differ from the previous one
    cleaned_chars = []
    for char in user_word:
        if not cleaned_chars or char != cleaned_chars[-1]:
            cleaned_chars.append(char)
            
    cleaned_word = "".join(cleaned_chars)
    print(f"Resulting word: '{cleaned_word}'")




 