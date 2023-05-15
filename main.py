from tkinter import Tk, Button, Label
import pygame


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
    
