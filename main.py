import math
import random
import sys
from tkinter import Tk, Button, Label
import numpy as np
import pygame


board = np.zeros((6, 7))
The_End = False
width = 7 * 100
height = (6 + 1) * 100
size = (width, height)
radius = int(100 / 2 - 5)


def createBoard():
    global board
    return board

def put_coin(board, row, col, piece):
    board[row][col] = piece

def isValidLocation(board, col):
    return board[6 - 1][col] == 0

def AvailabeRow(board, col):
    for r in range(6):
        if board[r][col] == 0:
            return r

def printBoard(board):
    print(np.flip(board, 0))

def Is_Winning(board, piece):
    # Check horizontal locations for win!!
    for c in range(7 - 3):
        for r in range(6):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win!!
    for c in range(7):
        for r in range(6 - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check positively sloped diaganoll!!
    for c in range(7 - 3):
        for r in range(6 - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check negatively sloped diaganol!!
    for c in range(7 - 3):
        for r in range(3, 6):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True


def isTerminalNode(board):
    return Is_Winning(board, 1) or Is_Winning(board, 2) or len(getValidLocation(board)) == 0

def MinMax(board, depth, maximizingPlayer):
    valid_locations = getValidLocation(board)
    is_terminal = isTerminalNode(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if Is_Winning(board, 2):
                return (None, 100000000000000)
            elif Is_Winning(board, 1):
                return (None, -10000000000000)
            # Game is over, no more valid moves!!
            else:
                return (None, 0)
        # Depth is zero!!
        else:
            return (None, 0)
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = AvailabeRow(board, col)
            b_copy = board.copy()
            put_coin(b_copy, row, col, 2)
            new_value = MinMax(b_copy, depth - 1, False)[1]
            if new_value > value:
                value = new_value
                column = col
            
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = AvailabeRow(board, col)
            b_copy = board.copy()
            put_coin(b_copy, row, col, 1)
            new_value = MinMax(b_copy, depth - 1, True)[1]
            if new_value < value:
                value = new_value
                column = col
        return column, value


def Alpha(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = getValidLocation(board)
    is_terminal = isTerminalNode(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if Is_Winning(board, 2):
                return (None, 1)
            elif Is_Winning(board, 1):
                return (None, -1)
            # Game is over, no more valid moves!!
            else:
                return (None, 0)
        # Depth is zero!!
        else:
            return (None, 0)
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = AvailabeRow(board, col)
            b_copy = board.copy()
            put_coin(b_copy, row, col, 2)
            new_score = Alpha(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = AvailabeRow(board, col)
            b_copy = board.copy()
            put_coin(b_copy, row, col, 1)
            new_score = Alpha(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def getValidLocation(board):
    valid_locations = []
    for col in range(7):
        if isValidLocation(board, col):
            valid_locations.append(col)
    return valid_locations




def drawBoard(board):
    screen = pygame.display.set_mode((700, 700))
    for c in range(7):
        for r in range(6):
            pygame.draw.rect(screen, (0, 0, 255), (c * 100, r * 100 + 100, 100, 100))
            pygame.draw.circle(screen, (0, 0, 0), (int(c * 100 + 100 / 2), int(r * 100 + 100 + 100 / 2)), radius)
    for c in range(7):
        for r in range(6):
            if board[r][c] == 1:
                pygame.draw.circle(screen, (255, 0, 0), (int(c * 100 + 100 / 2), height - int(r * 100 + 100 / 2)),radius)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, (255, 255, 0), (int(c * 100 + 100 / 2), height - int(r * 100 + 100 / 2)), radius)
    pygame.display.update()

def computer_move_random(board):
    available_columns = [col for col in range(7)]
    column = random.choice(available_columns)
    return column
The_End = False


def StartGame(optional,difficulty):
    pygame.init()
    screen = pygame.display.set_mode(size)
    board = createBoard()
    myfont = pygame.font.SysFont("monospace", 75)
    drawBoard(board)
    pygame.display.update()

    global The_End, Flag
    Flag=0 
    while not The_End:
        if Flag == 0:
                    col = computer_move_random(board)
                    if isValidLocation(board, col):
                        row = AvailabeRow(board, col)
                        put_coin(board, row, col, 1)

                        if Is_Winning(board, 1):
                            label = myfont.render("Player 1 wins!!", 1, (255, 0, 0))
                            screen.blit(label, (40, 10))
                            The_End = True

                        Flag += 1
                        Flag = Flag % 2

                        printBoard(board)
                        drawBoard(board)

                        

        # Ask for Player 2 Input!!
        if Flag == 1 and not The_End:
            if optional=="Min":
                if(difficulty=="Easy"):
                    col, minimax_score = MinMax(board, 3, True)
                elif(difficulty=="Medium"):
                    col, minimax_score = MinMax(board, 4, True)
                else :
                    col, minimax_score = MinMax(board, 5, True)
            else:
                if(difficulty=="Easy"):
                    col, minimax_score = Alpha(board, 3, -math.inf, math.inf, True)
                elif(difficulty=="Medium"):
                    col, minimax_score = Alpha(board, 4, -math.inf, math.inf, True)
                else :
                    col, minimax_score = Alpha(board, 5, -math.inf, math.inf, True)
            if isValidLocation(board, col):
                row = AvailabeRow(board, col)
                put_coin(board, row, col, 2)

                if Is_Winning(board, 2):
                    label = myfont.render("Player 2 wins!!", 1, (255, 255, 0))
                    screen.blit(label, (40, 10))
                    The_End = True

                printBoard(board)
                drawBoard(board)

                Flag += 1
                Flag = Flag % 2

        if The_End:
            pygame.time.wait(5000)
import time

# Function to measure the execution time and explore nodes using Minimax algorithm
def measure_minimax_performance(board, depth):
    start_time = time.time()
    MinMax(board, depth, True)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time
# Function to measure the execution time and explore nodes using Alpha-Beta Pruning algorithm
def measure_alphabeta_performance(board, depth):
    start_time = time.time()
    Alpha(board, depth, -math.inf, math.inf, True)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Create a table to compare performance
def compare_performance():
    board = createBoard()
    depths = [3, 4, 5]  # Different depths to test

    print("Depth\tMinimax Time\tAlpha-Beta Time\tAlpha-Beta Nodes")
    for depth in depths:
        minimax_time= measure_minimax_performance(board, depth)
        alphabeta_time= measure_alphabeta_performance(board, depth)
        print(f"{depth}\t{minimax_time:.6f}\t{alphabeta_time:.6f}")

# Run the comparison
compare_performance()

#Gui of start Screen
def algorithm_screen():
    def choose_option(option):
        start_screen.destroy()  # Close the start screen window
        difficulty_screen(option)

    start_screen = Tk()
    start_screen.title("Start Screen")
    start_screen.geometry("700x400")  # Set the window size to 400x300 pixels
    start_screen.configure(bg="#b39ddb") 

    title_label = Label(start_screen, text="Choose an option:", font=("Arial", 16))
    title_label.place(relx=0.5, rely=0.2, anchor="center")
    title_label.configure(bg="#b39ddb")

    min_button = Button(start_screen, text="Min Max Algorithm", font=("Arial", 12), width=20, height=2, bg="#7986cb", fg="#FFFFFF",
                        command=lambda: choose_option("Min"))
    min_button.place(relx=0.5, rely=0.4, anchor="center")  # Position the button in the center

    max_button = Button(start_screen, text="Alpha Beta Algorithm", font=("Arial", 12), width=20, height=2, bg="#7986cb", fg="#FFFFFF",
                        command=lambda: choose_option("Alpha"))
    max_button.place(relx=0.5, rely=0.6, anchor="center")  # Position the button in the center

    start_screen.mainloop()

#Gui to choose level
def difficulty_screen(option):
    def choose_difficulty(difficulty):
        print(f"You selected: {option} and {difficulty}")
        difficulty_screen.destroy()  # Close the difficulty selection screen
        # Start the game with the selected option and difficulty
        StartGame(option,difficulty)

    difficulty_screen = Tk()
    difficulty_screen.title("Difficulty Selection")
    if option == "Min":
        difficulty_screen.geometry("700x400")  # Set the window size for "Min" option
        difficulty_screen.configure(bg="#b39ddb") 
        
    elif option == "Max":
        difficulty_screen.geometry("700x400")
        difficulty_screen.configure(bg="#b39ddb") 

    easy_button = Button(difficulty_screen, text="Easy", font=("Arial", 12), width=15, height=2,bg="#7986cb", fg="#FFFFFF", command=lambda: choose_difficulty("Easy"))
    easy_button.place(relx=0.5, rely=0.4, anchor="center")

    medium_button = Button(difficulty_screen, text="Medium", font=("Arial", 12), width=15, height=2,bg="#7986cb", fg="#FFFFFF",command=lambda: choose_difficulty("Medium"))
    medium_button.place(relx=0.5, rely=0.6, anchor="center")

    hard_button = Button(difficulty_screen, text="Hard", font=("Arial", 12), width=15, height=2,bg="#7986cb", fg="#FFFFFF",command=lambda: choose_difficulty("Hard"))
    hard_button.place(relx=0.5, rely=0.8, anchor="center")


algorithm_screen()
