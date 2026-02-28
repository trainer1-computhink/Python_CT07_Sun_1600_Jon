print("Hello from lesson 6")

# # Lesson 6 - 2-dimensional list

# ## Recap 1: List of 100 unique numbers
# **Recap 1a**:
# You are preparing for an upcoming lucky draw session at your
# school. However, there must be no repeating winning numbers.

# Task: Create a program to create 100 random unique numbers in
# a list
# 1. Use a loop to add 100 random numbers into your list.
# 2. Each number added range between 1 to 1000
# 3. Ensure that all the numbers are unique

# **Recap 1b**:
# You have been asked to provide some statistics based on the
# list of numbers generated.

# 1. Using max(), find the highest number from the list
# 2. Using min(), find the lowest number from the list
# 3. Using sum() and len(), find the average from the list
# 4. By importing the 'random' library and using random.choice(),
#    print out a random number from the list.
# 5. Using index(), print out the index of the printed random
#    number.


# list_nums = [2, 3,4 ,5, 6, 7]
# print(list_nums)
# for num in list_nums:
#     print(num)


# students = [
#     ["Olivia", "F"], ["Noah", "M"], ["Emma", "F"],
#     ["Liam", "M"], ["Ava", "F"], ["Ethan", "M"],
#     ["Sophia", "F"], ["Lucas", "M"], ["Mia", "F"],
#     ["Aiden", "M"], ["Isabella", "F"], ["Jackson", "M"],
#     ["Amelia", "F"], ["Logan", "M"], ["Lily", "F"]
# ]

# boys = []
# girls = []

# for student in students:
#     name, gender = student
#     if gender == "F":
#         girls.append(name)
#     else:
#         boys.append(name)
# print(boys)
# print(girls)
# print(len(boys))
# print(len(girls))


a1 = [
    [1 , 2, 3],
    [4, 5, 6],
    [7, 8 ,9]
]

a2 = [
    [7 , 9, 3],
    [7, 5, 4],
    [1, 8 ,4]
]

# find a3 if i want to add for example [1,2,3] and [7,9,3] = [1+7, 2+9, 3+3]
# i want you to add each element at the respective to one another for a1 and a2
a3 = []

for i in range(len(a1)):
    for j in range(len(a1)):
        sum = a1[i][j] + a2[i][j]
        a3.append(a3[i].append(sum))