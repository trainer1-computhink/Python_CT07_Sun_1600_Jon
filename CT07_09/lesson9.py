# # Lesson 9 - Introduction to Functions

# ## Recap 1: Input Processing
# Create a program that will ask the riddle:
# - “What has to be broken before you can use it?”

# The user’s input is then processed to ensure that the user’s answer to the riddle is evaluated correctly regardless of capitalisation or additional non-relevant words.

# You may use the following steps as a guide:
# 1. Ask the user for a riddle and store their response in ‘userInput’ variable
# 2. Create an ‘isCorrect’ variable with the Boolean value ‘False’
# 3. Using ‘.lower()’, convert all letters of the user’s response to become lowercase
# 4. Use a ‘for’ loop to iterate through the list, using ‘if’ to check if any of the items in the list is “egg” If an item in the list is “egg”, change the variable ‘isCorrect’ to ‘True’
# 5. If ‘isCorrect’ is ‘True’, print “Correct! Well done.”
# 6. Else, print “That’s not correct. Try again!”

# All of the following responses must be evaluated as a correct answer:
# 1. An egg
# 2. EGG
# 3. eGG
# 4. Egg obviously
# 5. iT MuSt Be An EgG

# user_input = input("What has to be broken before you can use it?:\n").lower()
# is_correct = False
# user_input_list = user_input.split()
# for item in user_input_list:
#     if item == "egg":
#         is_correct = True
#         break
# if is_correct:
#     print("Correct! Well done.")
# else:
#     print("That's not correct. Try again!")
    
    


# ## Recap 2: Turtle drawing

# ### Recap 2a
# Using the ‘turtle’ library, create a 200x200 window
# Import the ‘turtle’ library
# Using ‘.setup()’, create a window 200 in width and 200 in height
# Add a ‘.mainloop()’ function to keep the window open
# import turtle
# window = turtle.Screen()
# window.setup(width=600,height=600)
# window.bgcolor("forestgreen")

# window.mainloop()

# ### Recap 2b
# Modify your previous code to create a blue arrow as your turtle.
# Create a turtle called “artist” using ‘turtle.Turtle()’
# Using ‘.shape()’, change the turtle shape to “arrow”
# Using ‘.color()’, change the turtle color to “blue”
# artist = turtle.Turtle()
# artist.shape("turtle")
# artist.color("blue")
# # artist.speed(5)
# # artist.seth(45)
# # artist.forward(100)
# # artist.seth(90)
# # artist.backward(50)
# # artist.seth(135)
# # artist.forward(100)
# # artist.seth(180)
# # artist.backward(50)
# # artist.seth(225)
# # artist.forward(100)
# # artist.seth(270)
# # artist.backward(50)
# # artist.seth(315)
# # artist.forward(100)
# # artist.seth(360)
# # artist.backward(50)
# # turtle.done()
# window.mainloop()

# ### Recap 2c
# Modify your previous code to draw the shape of a compass rose
# Use ‘.penup()’ and position turtle to (0, 0) using ‘.goto()’
# Point turtle towards North (“90”) using ‘.seth()’
# Use ‘.pendown()’ and draw “60” towards North
# Using ‘.right()’, turn turtle 90 degrees to the right
# Using a ‘for’ loop, draw a circle by moving 1 step each time before turning 1 degree to the right for 360 times.

# artist = turtle.Turtle()
# artist.speed(0)
# artist.shape("arrow")
# artist.color("blue")
# artist.goto(0,0)
# artist.seth(90)
# artist.pendown()
# artist.forward(60)
# artist.right(90)
# for i in range(1,361):
#     artist.forward(1)
#     artist.seth(-i)
#     print(f"Current turtle position: {artist.xcor()}, {artist.ycor()}")
# turtle.done()


# ### Recap 2d
# Modify your previous code to print the position of your turtle at the end of the drawing.

# Using ‘pos()’, print onto the console your turtle’s last coordinates in the following format:“Current turtle position: , ”

# ## Task 1: Square
# Using the ‘turtle’ library, create a function that draws a square.


# Use the function you have created to draw the pattern shown below:

# ☐☐☐☐☐☐
#   ☐☐☐☐
#    ☐☐

# 1. Import the ‘turtle’ library
# 2. Set up the screen using ‘turtle.Screen()’
# 3. Create a function, “draw_square” that will draw a 20x20 square
# 4. Using ‘for’ loops and the “draw_square” function you have created, draw the pattern shown on the screen.
# 5. You will have to reposition your turtle before calling the “draw_square” function each time.
# import turtle

# window = turtle.Screen()
# window.setup(width=600, height=600)
# window.bgcolor("forestgreen")

# t = turtle.Turtle()
# t.penup()
# t.speed(0)

# def draw_square():
#     t.pendown()
#     for i in range(4):
#         t.forward(20)
#         t.right(90)
#     t.penup()

# x = -100
# y = 100
# squares_in_row = 6

# for i in range(3):
#     t.goto(x, y)

#     for j in range(squares_in_row):
#         draw_square()
#         t.forward(25)

#     x += 25
#     y -= 35
#     squares_in_row -= 2

# turtle.done()


# ## Task 2: Square in a Square
# Use a function with parameters to draw 7 squares inside each other, getting smaller and smaller.

# 1. Import the ‘turtle’ library
# 2. Create a 400x400 screen
# 3. Create a function “draw_square” with a “size” parameter
# 4. The “draw_square” function will draw a square of size*size around the (0,0) coordinate.
# 5. Within a ‘for’ loop, use the “draw_square” function you have created to draw 7 squares around the (0,0) coordinate with the following sizes:50, 100, 150, 200, 250, 300, 350

# import turtle

# window = turtle.Screen()
# window.setup(width=400, height=400)
# window.bgcolor("forestgreen")

# t = turtle.Turtle()
# t.penup()
# t.speed(10)

# def draw_square(size):
#     t.goto(-size / 2, size / 2)
#     t.pendown()
#     for i in range(4):
#         t.forward(size)
#         t.right(90)
#     t.penup()

# for size in [50, 100, 150, 200, 250, 300, 350]:
#     draw_square(size)

# turtle.done()

# ## Task 3: Shape Creator
# You want to create a shape creator program that will draw any shape you want simply by giving the program the length and number of sides that the shape must have.

# To do this, you need to create a function with 2 parameters:
# - ‘length’
# - ‘num_sides’

# 1. Create a function called draw_shape() that takes in the length of the sides, as well as the number of sides.
# 2. The function should draw a shape with the length of sides and number of sides given by calculating the exterior angle
# 3. Using the  draw_shape() function, draw the following:
# - Pentagon, Hexagon, Octagon and Decagon


# import turtle

# window = turtle.Screen()
# window.setup(width=600, height=600)

# t = turtle.Turtle()
# t.speed(0)
# t.penup()

# def draw_shape(length, num_sides):
#     t.pendown()
#     for i in range(num_sides):
#         t.forward(length)
#         t.right(360 / num_sides)
#     t.penup()

# positions = [(-200, 250), (100, 250), (-200, 0), (100, 0)]
# sides_list = [5, 6, 8, 10]

# for i in range(4):
#     t.goto(positions[i])
#     draw_shape(80, sides_list[i])

# turtle.done()

# ## Task 4: Drawing a House
# You have been tasked to draw a house (made of a square and a triangle)

# Using the ‘draw_shape’ function you have just created, create a house by first drawing a square, then a triangle above the square.
# 1. The house is made up of a 100x100 square and a triangle that is 100 units long each side.
# 2. The triangle must be connected to the square

# You may refer to the following as a guide:
# 1. Import ‘turtle’ library
# 2. Set up a window
# 3. Create a turtle object and lift the pen to move without drawing
# 4. Define ‘draw_shape’ function to draw a regular polygon based on specified length and number of sides
# 5. Define ‘draw_house’ function that uses the ‘draw_shape’ function to combine a square and a triangle

import turtle

window = turtle.Screen()
window.setup(width=600, height=600)

t = turtle.Turtle()
t.speed(0)
t.penup()

def draw_shape(length, num_sides):
    t.pendown()
    for i in range(num_sides):
        t.forward(length)
        t.left(360 / num_sides)
    t.penup()

def draw_house(x, y):
    # draw square body
    t.goto(x, y)
    t.setheading(0)
    draw_shape(100, 4)

    # draw triangle roof
    t.goto(x, y + 100)
    t.setheading(0)
    draw_shape(100, 3)

draw_house(-50, -50)

turtle.done()