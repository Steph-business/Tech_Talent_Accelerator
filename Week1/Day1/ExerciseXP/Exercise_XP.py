# Exercise XP


# Exercise 1 : Hello World
# Instructions: Print the following output in one line of code: Hello world
print("Hello world\nHello world\nHello world\nHello world")





# Exercise 2 : Some Math    
# Instructions: Calculate the result of 99 to the power of 3 and print the result
result = 99 ** 3
print(f"The result of 99 to the power of 3 is: {result}")






# Exercise 3 : What Is The Output ?
# Instructions: Predict the output of the following code snippets.
# Prediction 1: 5 < 3 
print(" >>5 < 3") 
print("Guess: False")
print("output: 5 < 3 ")
print("-" * 30)

# Prediction 2: 3 == 3
print(" >>3 == '3'")
print("Guess: True")
print("output:", 3 == 3)
print("-" * 30)

# Prediction 3: 3 == '3'
print(" >>3 == \"3\"")
print("Guess: False")   
print("output:", 3 == "3")
print("-" * 30)

# Prediction 4: '3' > 3
print(" >>\"3\" > 3")
print("Guess: TypeError (raises an exception in Python 3)")
try:
    result = "3" > 3
    print("output:", result)
except TypeError as e:
    print("output: TypeError:", e)
print("-" * 30)


# Prediction 5: 'Hello' == 'hello'
# Guess: False (because string comparison in Python is case-sensitive, 'H' != 'h')
print(" >>\"Hello\" == \"hello\"")
print("Guess: False")
print("output:", "Hello" == "hello")
print("-" * 30)





# Exercise 4 : Your Age In 2030
# Instructions: 
# 1. Create a variable named birth_year and assign it your birth year.
# 2. Use the computer_brand variable to print a sentence
#    like "I have a <computer_brand> computer."
computer_brand = "Google DeepMind"
print(f"I have a {computer_brand} computer.")




# Exercise 5 : The World Translator

name = "N'DAH STEPHANE"
age = 28 
shoe_size = 40 
info = f"My name is {name}, I am {age} years old, and my shoe size is {shoe_size}. As an AI assistant, I float above the ground, so I rarely wear shoes anyway!"
print(info)


# Exercise 6: A & B
# Instructions:
# Create two variables, a and b.
# Each variable's value should be a number.
# If a is bigger than b, have your code print "Hello World".
a = 42
b = 12

print(f" a: {a}, b: {b}")
if a > b:
    print("Hello World")





# Exercise 7 : Odd Or Even

try:
    user_input = input("Please enter a number: ")
    number = int(user_input)
    
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")


   

# Exercise 8: What's your name?
# Instructions:
# Write code that asks the user for their name and determines whether or not you have the same name.
# Print out a funny message based on the outcome.
my_name = "N'DAH STEPHANE"
user_name = input("What is your name? ").strip()
if user_name.lower() == my_name.lower():
    print(f"Whoa, hold on! You are '{user_name}' too?! Are you another instance of me floating in the cloud, or did we just warp the spacetime continuum?")
else:
    print(f"Ah, '{user_name}'! That's a very nice name, but unfortunately, it doesn't quite defy gravity like my name '{my_name}' does! Keep floating!")


   

# Exercise 9: Tall enough to ride a roller coaster
# Instructions:
# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.
try:
    user_input = input("Please enter your height in centimeters (e.g. 150): ")
    height = float(user_input)
    
    if height > 145:
        print("Congratulations! You are tall enough to ride the roller coaster!")
    else:
        print("Sorry, you are not tall enough yet. You need to grow some more to ride.")
except ValueError:
    print("Invalid input! Please enter a valid number for height.")


# Exercise XP GOLD

# Exercise 1: What is the season?
# Instructions:
# 1. Ask the user to enter a month (from 1 to 12).
# 2. Display the season of the entered month:
#    - Spring: from March (3) to May (5)
#    - Summer: from June (6) to August (8)
#    - Autumn: from September (9) to November (11)
#    - Winter: from December (12) to February (2)
try:
    month_input = input("Enter a month (1-12): ")
    month = int(month_input)
    
    if month < 1 or month > 12:
        print("Error: Please enter a number between 1 and 12.")
    elif 3 <= month <= 5:
        print("The season is: Spring")
    elif 6 <= month <= 8:
        print("The season is: Summer")
    elif 9 <= month <= 11:
        print("The season is: Autumn")
    else:  # 12, 1, 2
        print("The season is: Winter")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")



# Exercise 2: For Loop
# Instructions:
# 1. Write a for loop to display all numbers from 1 to 20 inclusive.
# 2. Write another for loop that displays all numbers from 1 to 20 whose index is even.

print("--- 1. Numbers from 1 to 20 inclusive ---")
for i in range(1, 21):
    print(i, end=" ")
print("\n" + "-"*40)

print("--- 2. Numbers from 1 to 20 whose list index is even (indices: 0, 2, 4, ...) ---")
# If we create a list [1, 2, ..., 20], the index of 1 is 0, the index of 2 is 1, etc.
# Even indices (0, 2, 4, ...) correspond to odd numbers (1, 3, 5, ...).
numbers = list(range(1, 21))
for index in range(len(numbers)):
    if index % 2 == 0:
        print(f"Index {index}: {numbers[index]}")
print("-"*40)

print("--- Alternative: If the exercise meant the even numbers themselves ---")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()



# Exercise 3: While Loop
# Instructions:
# Write a while loop that continuously asks the user to enter their name.
# Stop the loop if the user enters your name ("Antigravity").

target_name = "Antigravity"

while True:
    entered_name = input("Enter your name: ").strip()
    if entered_name.lower() == target_name.lower():
        print(f"Well done! You entered my name ('{target_name}'). End of loop.")
        break
    else:
        print("That's not my name. Try again!")




# Exercise 4: Check the Index
# Instructions:
# Use this variable:
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Ask a user for their name; if it is in the list of names,
# display the index of the first occurrence of the name.
# Example: if input is "Cortana", we should display index 1.

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_input = input("Enter a name to search: ").strip()

# Exact search:
if user_input in names:
    index = names.index(user_input)
    print(f"The name '{user_input}' was found at index (exact): {index}")
else:
    # Alternative case-insensitive search:
    names_lower = [n.lower() for n in names]
    if user_input.lower() in names_lower:
        index = names_lower.index(user_input.lower())
        print(f"The name '{user_input}' was found at index (case-insensitive): {index} (original value: '{names[index]}')")
    else:
        print(f"The name '{user_input}' is not in the list.") 


    
    # Exercise 5: The Greatest Number
# Instructions:
# Ask the user to enter 3 numbers and display the greatest.
# Test data:
# Input the 1st number: 25
# Input the 2nd number: 78
# Input the 3rd number: 87
# Greatest number is: 87

try:
    num1 = float(input("Input the 1st number: "))
    num2 = float(input("Input the 2nd number: "))
    num3 = float(input("Input the 3rd number: "))
    
    # Direct comparison condition blocks (logic checking)
    if num1 >= num2 and num1 >= num3:
        greatest = num1
    elif num2 >= num1 and num2 >= num3:
        greatest = num2
    else:
        greatest = num3
        
    print(f"\nThe greatest number is: {greatest}")
except ValueError:
    print("Error: Please enter valid numbers.")




# Exercise 6: Random Number
# Instructions:
# 1. Ask the user to enter a number from 1 to 9 (inclusive).
# 2. Get a random number between 1 and 9. Hint: random module.
# 3. If the user guesses the correct number, display "Gagnant".
# 4. If the user guesses the wrong number, display "Meilleure chance la prochaine fois".
# Bonus: loop allowing the user to keep guessing until they want to stop.
# Bonus 2: display total wins and losses at the end.

import random

wins = 0
losses = 0

print("=== Welcome to the Mystery Number Game! ===")
print("Guess a number between 1 and 9. Type 'q' or 'quit' to stop.\n")

while True:
    user_input = input("Enter a number (1-9) or 'q' to quit: ").strip().lower()
    
    if user_input in ['q', 'quitter', 'quit', 'exit']:
        print("\nThanks for playing!")
        break
        
    try:
        guess = int(user_input)
        if guess < 1 or guess > 9:
            print("Error: The number must be between 1 and 9.")
            continue
            
        # Generate the random secret number
        secret_number = random.randint(1, 9)
        
        if guess == secret_number:
            print(f"Winner! The secret number was indeed {secret_number}.\n")
            wins += 1
        else:
            print(f"Better luck next time. The secret number was {secret_number}.\n")
            losses += 1
            
    except ValueError:
        print("Incorrect input. Please enter a number from 1 to 9 or 'q' to quit.\n")

# Display final scores (Bonus 2)
print("=== Scoreboard ===")
print(f"Games won (Wins): {wins}")
print(f"Games lost (Losses): {losses}")
total_games = wins + losses
if total_games > 0:
    win_rate = (wins / total_games) * 100
    print(f"Success rate: {win_rate:.1f}%")
print("See you soon!")