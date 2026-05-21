# Challenge 1: Multiples Generator
try:
    number = int(input("Enter the number: "))
    length = int(input("Enter the length: "))
    if length < 0:
        print("Error: length must be >= 0")
    else:
        multiples = [number * i for i in range(1, length + 1)]
        print(multiples)
except ValueError:
    print("Error: enter valid integers")


# Challenge 2: Remove Consecutive Duplicates
word = input("Enter a word: ").strip()
if not word:
    print("Error: empty word")
else:
    cleaned = []
    for c in word:
        if not cleaned or c != cleaned[-1]:
            cleaned.append(c)
    print("Result:", "".join(cleaned))








# Challenge 2: Remove Consecutive Duplicates
