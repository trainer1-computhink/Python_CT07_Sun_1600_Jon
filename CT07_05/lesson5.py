# print("Hello from lesson 5")
import random
# # num_list = []
# # for i in range(10):
# #     ran_num = random.randint(0,10)
# #     if not ran_num in num_list:
# #         num_list.append(ran_num)
# # print(num_list)
# # print(len(num_list))

# # while loop ? 
# # when to break out of the loop?
# # when you your list length == 100

# # for i in range(100):
# #     num_list .append(random.randint(65,100))
    
# # print(num_list)
# namelist = ["Olivia", "Liam", "Emma", "Noah", "Ava", "Ethan",
# "Sophia", "Lucas", "Mia", "Aiden"]

# heightlist = [160, 165, 158, 170, 162, 168, 159, 172, 164, 166]
# print(sum(heightlist))
# print(len(heightlist))
# print(sum(heightlist)/len(heightlist))
# print(min(heightlist))
# print(max(heightlist))

# min_height = min(heightlist)
# min_height_ind = heightlist.index(min_height)
# print(min_height_ind)
# #by knowing the namelist and the index of the shortest, how do we know the person name?
# min_height_name = namelist[min_height_ind]
# print(min_height_name)


# print(num_list.index(3))

## Task 5: Pokemon, I choose you!
# Task: You are given 2 lists,
# **pokemons** contains a list of pokemons
# **powers** contains a list of the corresponding pokemon's
#            powers

# 1. Choose 2 random pokemons from the list
# 2. Compare the powers of the 2 pokemons
# 3. Calculate who is the winner of the fight between these 2
#    pokemons
#    (pokemon with the higher power will always win)

# Sample data (Copy + paste the below code):
pokemons = [
    "Pikachu", "Charizard", "Bulbasaur", "Squirtle",
    "Jigglypuff", "Meowth", "Psyduck", "Eevee", "Snorlax",
    "Mewtwo", "Lapras", "Gengar", "Dragonite", "Machamp",
    "Arcanine", "Alakazam", "Gyarados", "Vaporeon", "Scyther",
    "Electabuzz"
]

pokemon1 = random.choice(pokemons)
pokemon2 = random.choice(pokemons)
print(pokemon1, pokemon2)

pokemon1_index = pokemons.index(pokemon1)
pokemon2_index = pokemons.index(pokemon2)
print(pokemon1_index, pokemon2_index)

powers = [
    55, 84, 49, 48, 45,
    45, 52, 55, 110, 110,
    85, 65, 134, 130, 110,
    50, 125, 65, 110, 83
]

pokemon1_powers = powers[pokemon1_index]
pokemon2_powers = powers[pokemon2_index]
print(pokemon1_powers, pokemon2_powers)

if pokemon1_powers > pokemon2_powers:
    print(pokemon1 + " wins.")
elif pokemon1_powers < pokemon2_powers:
    print(pokemon2 + " wins")
else:
    print("It is a tie between " + pokemon1 + " and " + pokemon2)

# Hint: import the random library and use random.choice(listname)