# Lesson 8 - Input Validation

## Recap 1: List Manipulation
# You have a list of student index numbers who attended the Math Enrichment class. 
# However, some students’ attendance were recorded more than once due to a human error.
# Your task is to clean the list and produce a list of unique Student Indexes

# Given a list of student index numbers (with duplicates), create a cleaned list where each student appears once.
# Sort the cleaned list in ascending order.
# - Print the final list and also print how many duplicates were removed.
# - Print the count of how many students attended the Math Enrichment Class.

student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]

duplicate_count = 0
unique_list = []
duplicate_list = []
for index in student_indexes:
    if index not in unique_list:
        unique_list.append(index)
    else:
        duplicate_count += 1
        duplicate_list.append(index)

# print(unique_list)

# sorted_list = sorted(unique_list)
# print(sorted_list)

# print(f"The final list is {sorted_list} and {duplicate_count} were removed, {len(sorted_list)} attended the class")

# student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]
# sorted_list = sorted(student_indexes)
# print(sorted_list)
# nested_list = []
# for index in unique_list:
#     if index in duplicate_list:
#         nested_list.append([index,index])
#     else:
#         nested_list.append([index])
# print(nested_list)
## Task 1: Data Format Check

### Task 1a
# Ask the user to input their first name until it is a valid name. 
# A valid name only contains alphabets.
# Keep asking for a name until a valid name is input.

# first_name = ""
# while not first_name.isalpha():
#     first_name = input("What is your first name?")
# print(first_name)


# while True:
#     first_name = input("What is your first name?")
#     if first_name.isalpha():
#         break
# print(first_name)

### Task 1b
# Ask the user to input their age until it is a valid number. 
# Keep asking for a name until a valid number is input.

# while True:
#     age = input("What is your age?")
#     if age.isdigit():
#         break
#     else:
#         print("Input only numbers")
# print(f"Age is {age}.")

### Task 1c
# Ask the user to input a valid username. A valid username must contain alphabets and numbers, but not contain special characters

# while True:
#     username = input("What is your username? ")
#     if username.isalnum():
#         break
# print(f"Username is {username}")

## Task 2: Length Check (using a while loop)

### Task 2a
# Ask the user to input their phone number until it is valid using a while loop.
# Make sure to check if the input is the correct data type as well!

# while True:
#     phone_number = input("What is your phone number? ")
#     if len(phone_number) == 8 and phone_number.isdigit():
#         break
# print(f"My phone num is {phone_number}")

### Task 2b
# Ask the user to a username and check if it is between 5 to 18 characters long.

## Task 3: Range Check (using a while loop)

### Task 3a
# Ask the user to input their birth year and check if it is between 1900 and the current year. Keep asking until a correct value is given.

# while True:
#     birth_year = input("What is your birth year? ")
#     if int(birth_year) > 1900 and int(birth_year) < 2027:
#         break
#     else:
#         print("It is invalid.")

print("A".isupper())
print("a".upper())
sentences = "Charizard and Dragonite are flying type."
new_sentences = ""
for i in range(len(sentences)):
    if i%2 == 0:
        new_sentences += sentences[i].lower()
    else:
        new_sentences += sentences[i].upper()
print(new_sentences)


### Task 3b
# Ask the user to input their volume setting and check if it is between 0 and 100.

## Task 4: Mocking Text Generator
# Create a program that will turn regular sentences into a “SpongeBob Mocking” meme.
# For example, the program will turn “Hello my name is James” into “HeLlO mY nAmE iS jAmEs”

# 1. Using input(), ask the user for a sentence
# 2. Use loops to iterate through each letter in the sentence
# 3. Alternate between .upper() and .lower() for each letter
# 4. Print the result.



## Task 5: Slice String
# word = “SINGAPORE”

# Slice the string and print these words:
# a. SING
# b. GAP
# c. PORE
# d. SNAOE

## Task 6: Palindrome
# Ask the user for an input and check if it is a palindrome, until the input is ‘end’.

# You can try this list of words:
# - civic, kayak, level, madam, radar, refer, rotator, tenet, racecar, deified, stats, wow

## Task 7: Presence and Existence Checks
# You are hosting a Birthday Party and have invited your friends.

# Create a list with your friends’ names
# - e.g. [“Alice”, “Bob”, Carl”, “Dylan”]

# Write a program to ask for the visitor’s name and check if:
# - Name is entered (presence check)
# - Name is in your friend list (existence check)

# Ask for an input again if a name was not entered.
# Accept the visitor if they are in the list, else deny their entry.

## Task 8: Format Check
# Ask the user to input their NRIC you need to check:
# 1. First and last character are alphabets in upper case
# 2. First letter must be S, T, F, G, or M.
# 3. Have 7 digits between the alphabets
# 4. Be 9 characters long

## Task 9: Password Validation
# A website requires all passwords to
# 1. Be at least 8 characters long
# 2. Contain an upper and lower case
# 3. Contain a number
# 4. No other characters except alphabets or numbers.

# Write a program that will ask the user for a password, and check if the password fits all criteria

# You may use some of the following passwords to test your program:
# - PassW0rd
# - H3ll0W0r1d
# - BestF00d
# - pa55Me
