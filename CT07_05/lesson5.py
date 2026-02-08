print("Hello from lesson 5")
import random
num_list = []
for i in range(10):
    ran_num = random.randint(0,10)
    if not ran_num in num_list:
        num_list.append(ran_num)
print(num_list)
# print(len(num_list))

# while loop ? 
# when to break out of the loop?
# when you your list length == 100

# for i in range(100):
#     num_list .append(random.randint(65,100))
    
# print(num_list)
# namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
# "Sophia", "Lucas", "Mia", "Aiden"]

# heightlist = [160, 165, 158, 170, 162, 168, 159, 1,72, 164, 166]
print(num_list.index(3))