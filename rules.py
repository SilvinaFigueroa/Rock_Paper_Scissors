# Rock - Paper - Scissors Game
# IT 111 Final project

# importing modules to use in our game:
from time import sleep
import random
import winsound


# Emojis to add a better user experience to our game!
# TODO Capitalize constants
emoji_rock = '\U0001FAA8'
emoji_scissors = '✂'
emoji_paper = '\U0001F4C3'
emoji_winner = '\U0001F389'
emoji_losser = '\U0001F3F4'
emoji_starface = '\U0001F929'


# Create a dictionary with the game options as numbers (to avoid user misspelling)
options = {1: "Rock", 2: "Paper", 3: "Scissors"}

class Game:
    def __init__(self):
        self.first_player = ""
        self.second_player = ""
        self.round = 0
        self.winner_player = 0
        self.winner_CPU = 0
        self.CPU_move = 0
        self.user_move = 0


    # Initialize game!
    # TODO decide if this is going to be called when the object is created (we need to add the __init__ function)
    def initialize(self):
        print("--------------------------------------------------------------\n")
        print(f'{emoji_starface}  Welcome to Rock {emoji_rock}  Paper, {emoji_paper}  Scissors {emoji_scissors}  Game! {emoji_starface} \n')
        print("--------------------------------------------------------------\n")
        sleep(0.3)

        #Traffic ligths emojis in an array (red - yellow - green)
        messages = ['\U0001F7E0', '\U0001F7E1', '\U0001F7E2']
        #Use sleep for delay the message pring and windsound to add a beep to the traffic ligths    
        for instructions in messages:
            print(instructions, end="  ", flush=True)
            winsound.Beep(700,400)
            sleep(0.7)

        print('GO! \U0001F3C1')
        winsound.Beep(1400,800)

        # We generate a random number between 1 and 3 to decide what choice the CPU will make
        self.CPU_move = random.randint(1, 3)

        # User player turns
        sleep(0.9)
        print("\n")
        print("--------------------------------------------------------------\n")
        print("Please choose one of the following options:\n")
        print("--------------------------------------------------------------\n")
        sleep(0.5)
        print(f'1. {options[1]} {emoji_rock} \n')
        sleep(0.5)
        print(f'2. {options[2]} {emoji_paper} \n')
        sleep(0.5)
        print(f'3. {options[3]} {emoji_scissors} \n')
        sleep(0.5)
    
        # User input 
        self.user_move = int(input())
        sleep(0.9)
        #Validation for user input
        if self.user_move == 1:
            print("\n")
            print(f'You chose {options[1]} {emoji_rock}')
        elif self.user_move == 2:
            print("\n")
            print(f' You chose {options[2]} {emoji_paper}')
        elif self.user_move == 3:
            print("\n")
            print(f'You chose {options[3]} {emoji_scissors}')
        else:
            print("\n")
            print("\nPlease enter a number between 1 and 3!")

    # Compare user input with CPU and determine a winner of that round
    def round_result(self):
        print("--------------------------------------------------------------\n")
        print (f'CPU chose {options[self.CPU_move]}')
        print("--------------------------------------------------------------\n")

        sleep(0.3)
        if (self.CPU_move == 1 and self.user_move == 2) or (self.CPU_move == 2 and self.user_move == 3) or (self.CPU_move == 3 and self.user_move == 1):
            print(f'User Player won this round {emoji_winner}')
            self.winner_player = self.winner_player + 1
        elif (self.CPU_move == 1 and self.user_move == 3) or (self.CPU_move == 2 and self.user_move == 1) or (self.CPU_move == 3 and self.user_move == 2):
            print(f'CPU won this round {emoji_losser}')
            self.winner_CPU = self.winner_CPU + 1
        else:
            print(f'( It\'s a tie! {emoji_starface}')
        # round is user to count each round and stop the game after 3 rounds
        self.round = self.round + 1

    # Switch users after each round
    def next_round(self):
        if (self.first_player == "Player"):
            self.first_player = "CPU"
            self.second_player = "Player"
            print(f'For next Round, {self.first_player} will start first!')
        else:
            self.first_player = "Player"
            self.second_player = "CPU"
            print(f'For next Round, {self.first_player} will start first!')


    # TODO: define a function that show the game rules with user input (if we have time)

    # TODO: define a function to set the best of 3 games and determine a winner for the game

    # use the variables Round and winner counter already set in the beginning of the game

    # TODO assign names to the user player? It's a nice to have (if we have time).

    # user input that  overrides the variable user player name

    # TODO: Show to user each round and partial results of each round (if we have time)

        # Round (#): print emoji_winner
        # Round results: print emoji_winner
        # Parcial results: CPU won (x times) Player won (y times)
