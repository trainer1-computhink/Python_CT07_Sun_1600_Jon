print("Hello from lesson 2")

# # count from 100 to 1
# for count in range(100,0,-1):
#     print(count)

# count = 1
# for i in range(5):
#     for j in range(2):
#         print(f"bababa " + str(count) +" times")
#         count += 1

# for i in range(20):
#     if i%7 == 0:
#         print(i)

print("toppings " + "abc")


# ## Task 5: General Knowledge Quiz
# **Task: Create a program to quiz users on their general
# knowledge**

# Using the while loop, ask 3 general knowledge questions
# 1. Using input ask the question
# 2. While answer is not correct, repeat the question.
# 3. Move on to the next question when the answer is correct

# Bonus:
# 1. Add a score system
# 2. Add an ability for users to skip by saying “skip”
# 3. Disqualify user when they have tried too many times


while True:
    question1 = input("Who painted the famous artwork 'Mona Lisa' ?").lower().strip()
    if question1 == "leonardo da vinci":
        break
    print("The answer is wrong try again.")

print("The answer is correct.")

while True:
    question2 = input("What is the name of the planet that we stay on?").lower().strip()
    if question2 == "earth":
        break
    print("The answer is wrong try again.")
print("The answer is correct.")