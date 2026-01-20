import turtle
import time

# --- Configuration Constants ---
BOARD_SIZE = 800
CELL_SIZE = BOARD_SIZE // 3
clicked_row = -1
clicked_col = -1
screen = turtle.Screen()
pen = turtle.Turtle()

# The list of all 8 winning combinations (rows, columns, diagonals)
WIN_CONDITIONS = [
    [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], # Rows
    [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)], # Columns
    [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]  # Diagonals
]

# --- Global Variables and Setup ---
def setup_turtle():
    """Configures the turtle screen and pen settings."""
    screen.setup(width=BOARD_SIZE, height=BOARD_SIZE)
    screen.title("Turtle Tic Tac Toe")
    # Tell turtle that the bottom-left corner of the window is coordinate (0, 0) and the top-right corner is (BOARD_SIZE, BOARD_SIZE). This simplifies the math needed to draw things at specific pixel locations.
    screen.setworldcoordinates(0, 0, BOARD_SIZE, BOARD_SIZE)
    # screen.tracer(0) # Turn off automatic animations
    pen.speed(10)
    pen.hideturtle()
    pen.pensize(5)

# --- Game Logic Functions ---
def initialise_board():
    """Creates a fresh, empty 3x3 board."""
    board = []
    for _ in range(3):
        row = []
        for _ in range(3):
            row.append(' ')
        board.append(row)
    return board

def check_full(board):
    """Checks if the board is full and there is a draw."""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def check_win(board, player):
    """Checks if the specified player has won using the win_conditions list."""
    for condition in WIN_CONDITIONS:
        # Check if all three cells in the current winning condition match the player's marker
        if all(board[r][c] == player for r, c in condition):
            return True
    return False

def switch_player(current_player):
    """Switches the current player between 'X' and 'O'."""
    if current_player == 'X':
        return 'O'
    else:
        return 'X'

# --- Turtle Drawing Functions ---
def draw_board_grid():
    """Draws the main grid lines for the board."""
    pen.penup()
    for i in range(1, 3):
        # Draw vertical lines
        pen.goto(i * CELL_SIZE, 0)
        pen.pendown()
        pen.goto(i * CELL_SIZE, BOARD_SIZE)
        pen.penup()
        # Draw horizontal lines
        pen.goto(0, i * CELL_SIZE)
        pen.pendown()
        pen.goto(BOARD_SIZE, i * CELL_SIZE)
        pen.penup()

def draw_x(x, y):
    """Draws an 'X' in red."""
    padding = CELL_SIZE * 0.05
    pen.pencolor("red")
    pen.penup()
    pen.goto(x + padding, y + padding)
    pen.pendown()
    pen.goto(x + CELL_SIZE - padding, y + CELL_SIZE - padding)
    pen.penup()
    pen.goto(x + CELL_SIZE - padding, y + padding)
    pen.pendown()
    pen.goto(x + padding, y + CELL_SIZE - padding)
    pen.penup()
    pen.pencolor("black")

def draw_o(x, y):
    """Draws an 'O' in blue."""
    radius = CELL_SIZE * 0.4
    pen.pencolor("blue")
    pen.penup()
    pen.goto(x + CELL_SIZE / 2, y + CELL_SIZE / 2 - radius)
    pen.pendown()
    pen.circle(radius)
    pen.penup()
    pen.pencolor("black")

def draw_marker(row, col, marker):
    """Calculates the center coordinates and draws the specific marker."""
    start_x = col * CELL_SIZE
    start_y = (2 - row) * CELL_SIZE
    
    if marker == 'X':
        draw_x(start_x, start_y)
    elif marker == 'O':
        draw_o(start_x, start_y)
    # screen.update()

def display_message(message):
    """Writes a message centrally onto the turtle screen."""
    pen.penup()
    pen.goto(BOARD_SIZE / 2, BOARD_SIZE / 2 - 50) 
    pen.pencolor("black")
    pen.write(message, align="center", font=("Arial", 32, "bold"))
    # screen.update()

# --- Event Handling ---

def handle_click(x, y):
    """Translates screen coordinates into 0-indexed row and column indices."""
    global clicked_row, clicked_col
    col = int(x // CELL_SIZE)
    row = int((BOARD_SIZE - y) // CELL_SIZE)
    
    if 0 <= row < 3 and 0 <= col < 3:
        clicked_row = row
        clicked_col = col

def get_player_move_turtle(current_player, board):
    global clicked_row, clicked_col
    screen.onclick(handle_click)
    
    valid_move = False
    while not valid_move:
        turtle.update() 
        if clicked_row != -1 and clicked_col != -1:
            row = clicked_row
            col = clicked_col
            if board[row][col] == ' ':
                board[row][col] = current_player
                draw_marker(row, col, current_player)
                valid_move = True
            else:
                print("Spot already taken! Choose again.")
                clicked_row = -1
                clicked_col = -1
        time.sleep(0.01)
        
    screen.onclick(None)
    clicked_row = -1
    clicked_col = -1

# --- Main Game Loop ---

def main_game_loop():
    setup_turtle()
    draw_board_grid()
    # screen.update()
    board = initialise_board()
    current_player = 'X'

    while True:
        get_player_move_turtle(current_player, board)
        
        if check_win(board, current_player):
            display_message(f"Player {current_player} wins!")
            break
        
        elif check_full(board):
            display_message("It's a draw!")
            break
        
        current_player = switch_player(current_player)

    screen.mainloop()

if __name__ == "__main__":
    main_game_loop()

# CELL_SIZE:
#     This is the most important constant. It defines the exact width and height of a single square (or cell) on your board (e.g., 400 pixels when your BOARD_SIZE was 1200).
#     All other drawing dimensions are based on this number.
# padding:
#     This is the small amount of empty space added around the edges of the markers.
#     For the 'X' marker, we used a 5% padding (CELL_SIZE * 0.05). This prevents the diagonal lines of the 'X' from touching or overlapping the thick grid lines, making the board look cleaner.
# radius:
#     This term is specific to drawing the 'O' marker. The turtle.circle() function requires a radius measurement.
#     We used a radius that was 40% of the cell size (CELL_SIZE * 0.4), which makes the 'O' fit nicely within the cell, respecting the padding.
#     Essentially, CELL_SIZE defines the boundary you are drawing in, while padding and radius define how big the marker is relative to that boundary.

# Setup & Initialization (Building the foundation)
#     setup_turtle(): Configures the window size, title, and drawing tools (the pen).
#     initialise_board(): Creates the internal data structure (a list of lists) that keeps track of where 'X's and 'O's are placed in the computer's memory.
#     draw_board_grid(): Uses the pen to draw the visible lines on the screen.

# Game State Logic (The rules of Tic Tac Toe)
#     check_win(): Evaluates the board data to see if a player has three markers in a row.
#     check_full(): Checks the board data to see if all nine spots are filled, signaling a potential draw.
#     switch_player(): Alternates the current turn between 'X' and 'O'.

# User Interaction (Input and Output)
#     handle_click() and get_player_move_turtle(): These functions work together to detect mouse clicks, translate the click position into a valid spot on the internal board data, and make sure the spot is empty.
#     draw_marker(): Calls either draw_x() or draw_o() to visually update the screen after a valid move is made.
#     display_message(): Writes text (like "Player X wins!") directly onto the graphical screen when the game ends.

# Program Execution (The overall flow)
#     main_game_loop(): This is the orchestrator. It runs the game turn by turn, calling all the other functions in the correct order to manage a complete game from start to finish.


# Setup & Initialization
# setup_turtle():
# Details: Configures the turtle screen object (screen). It uses the global BOARD_SIZE variable to set the window dimensions. Crucially, screen.setworldcoordinates(0, 0, ...) redefines the coordinate system so that we can easily work with positive pixel values starting from the bottom-left corner. screen.tracer(0) is used to prevent animations and allow manual updates for smoother drawing.

# initialise_board():
# Details: This function is pure Python logic. It uses a nested for loop (a loop inside a loop) to create a list that contains three more lists inside it. This 2D array structure ([[' ', ' ', ' '], ... ]) is the fundamental data model the entire game uses. It returns this blank board state.

# draw_board_grid():
# Details: Uses the pen.goto() and pen.pendown() methods to move the pen without drawing and then draw the vertical and horizontal lines of the grid. It relies on the global CELL_SIZE variable to determine where to place the lines (at 1 * CELL_SIZE and 2 * CELL_SIZE).
# Game State Logic

# check_full(board):
# Parameters: Takes the current board data (the list of lists).
# Details: Iterates through every cell of the board using nested loops. If it finds even one empty space (' '), it immediately stops and returns False (meaning not full). If the loops finish without finding an empty spot, it means the board is full and it returns True.

# check_win(board, player):
# Parameters: Takes the current board data and the player marker being checked ('X' or 'O').
# Details: This function uses the WIN_CONDITIONS list we defined globally. It iterates through all 8 conditions. It uses a Python generator expression (all(...)) to efficiently check if every coordinate within that condition matches the specified player's marker. Returns True if any condition is met.

# switch_player(current_player):
# Parameters: Takes the current player's marker.
# Details: A simple if/else statement that performs the turn swap. It is called at the very end of a turn in the main game loop if no win or draw occurs.
# User Interaction (Input and Output)

# handle_click(x, y):
# Parameters: Receives the raw x and y pixel coordinates automatically from the turtle library when a click happens.
# Details: This is a crucial "callback" function. It translates raw pixels into game coordinates (row, col from 0 to 2) using integer division (// CELL_SIZE). It then updates the global variables clicked_row and clicked_col, which signals to the main game loop that a click has occurred.

# get_player_move_turtle(current_player, board):
# Parameters: Takes the current player and the board state.
# Details: This function manages the input loop. It binds the handle_click function using screen.onclick(). It enters a while not valid_move: loop that effectively pauses the game flow (using time.sleep(0.01) to prevent CPU overuse) until a valid move is registered by the handle_click function.

# draw_marker(row, col, marker):
# Parameters: Takes the game's row, col, and marker type.
# Details: Calculates the exact pixel location for the marker using the CELL_SIZE constant and calls the specific drawing helper functions (draw_x or draw_o). It calls screen.update() to make the drawing instantly visible.

# draw_x() & draw_o():
# Details: These functions handle specific drawing commands. They use pen.pencolor() to set red/blue colors, use the padding or radius variables to size the shapes correctly, and reset the pen color to black afterward.

# display_message(message):
# Parameters: Takes the game end message text.
# Details: Uses pen.write() to display text on the screen. It centers the text and uses a large font for visibility.

# Program Execution
# main_game_loop():
# Details: This is where the program execution starts after the if __name__ == "__main__": block runs. It calls all the setup functions, initializes the game state, and then runs the main while True: loop that coordinates every turn, checks the outcomes, and switches players until a win or draw breaks the loop. Finally, it calls screen.mainloop() to keep the graphical window open after the game ends.