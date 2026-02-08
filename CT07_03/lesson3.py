# print("Hello from lesson 3")

# import time
# # for i in range(10,0,-1):
# #     print(i)


# # for i in range(10,-1,-1):
# #     time.sleep(1)
# #     print(i)

# # ## Task 1: Study Timer
# # **Task: Write a program that acts as a study timer**
# # 1. The user must input how many minutes they plan to study
# # 2. Use a while loop to count down the minutes
# # 3. Display "Good job!" once the timer is up

# # 15 min 
# # 14 min 

# timer = int(input("How many mins?"))
# while True:
    
#     if timer <= 0:
#         break
    
#     print(f"{timer} mins left")
#     time.sleep(3)
#     timer -= 1
# print("good job")

# ## Task 3: Multiplication Quiz
# **Task: Ms Tan, your math teacher knows that you are a
# programming whiz,
# she has asked you to help code a multiplication quiz for
# the class to practice.**

# Here are her requirements:
# 1. Students have to answer 15 questions in total
# 2. Students have 3 lives (chances). i.e. they can get the
#    question wrong 3 times.
# 3. The questions will be in this format: "What is 3 x 19? ". 
# 4. The numbers for each question will be randomly generated
#    and between the range of 2 to 20.
# 5. If the student answers correctly, move on to the next
#    question
# 6. If the student answers wrongly, minus 1 life, and ask
#     the question again.
# 7. If the student has no more lives, exit and print
#     "GO AND SEE MS TAN FOR REMEDIAL"

import random

num_qns = 3
lives = 3

for i in range(num_qns):
    num1 = random.randint(2,20)
    num2 = random.randint(2,20)
    correct_ans = num1 * num2

    while lives > 0:
        ans = int(input(f"What is {num1} x {num2} ?"))

        if ans == correct_ans:
            print("Correct")
            break

        else:
            lives -= 1
            print("Wrong answer! Try again")

        if lives == 0:
            print("GO AND SEE MS TAN FOR REMEDIAL")
            break

    if lives == 0:
        break

if lives > 0:
    print("Well done")
    

