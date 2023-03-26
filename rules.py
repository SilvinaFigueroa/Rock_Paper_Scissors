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
emoji_book = '\U0001F4D6'

# Create a dictionary with the game options as numbers (to avoid user misspelling)
options = {1: "Rules", 2: "Rock", 3: "Paper", 4: "Scissors"}

class Game:
    def __init__(self):
        self.first_player = ""
        self.second_player = ""
        self.round = 0
        self.winner_player = 0
        self.winner_CPU = 0
        self.CPU_move = 0
        self.user_move = 0

    def print_options(self):
        sleep(0.9)
        print("\n")
        print("--------------------------------------------------------------\n")
        print("Please choose one of the following options:\n")
        print("--------------------------------------------------------------\n")
        sleep(0.5)
        print(f'1. {options[1]} {emoji_book} \n')
        sleep(0.5)
        print(f'2. {options[2]} {emoji_rock} \n')
        sleep(0.5)
        print(f'3. {options[3]} {emoji_paper} \n')
        sleep(0.5)
        print(f'4. {options[4]} {emoji_scissors} \n')
        sleep(0.5)
    
    def print_welcome(self):

        print("--------------------------------------------------------------\n")
        print(f'{emoji_starface} Welcome to Rock {emoji_rock}  Paper {emoji_paper} Scissors {emoji_scissors} Game! {emoji_starface} \n')
        print("--------------------------------------------------------------\n")
        sleep(0.3)

        #Traffic ligths emojis in an array (red - yellow - green)
        messages = ['\U0001F7E0', '\U0001F7E1', '\U0001F7E2']
        #Use sleep for delay the message pring and windsound to add a beep to the traffic ligths
        for instructions in messages:
            print(instructions, end=" ", flush=True)
            winsound.Beep(700,400)
            sleep(0.7)

        print('GO! \U0001F3C1')
        winsound.Beep(1400,800) 

    # Initialize game!
    # TODO decide if this is going to be called when the object is created (we need to add the __init__ function)
    def initialize(self):

        self.print_welcome()
        self.print_options()

        # We generate a random number between 1 and 3 to decide what choice the CPU will make
        self.CPU_move = random.randint(2, 4)
        
        # User input (User player turns)
        self.user_move = int(input())
        sleep(0.9)
        self.options_validation()

        #Validation for user input
    def options_validation(self):
        if self.user_move == 1:
            print("\n")
            print(f'You chose {options[1]}!\n')
            print('The rules of rock, paper, scissor are:\n')
            print('Rock beats scissor, scissor beats paper, and paper beats rock\n')
            print('To start playing, retry and pick a number 2-4')
            self.print_options()
            # User input (User player turns)
            self.user_move = int(input())
            sleep(0.9)
            self.options_validation()

        elif self.user_move == 2:
            print("\n")
            print(f'You chose {options[2]} {emoji_rock}')
        elif self.user_move == 3:
            print("\n")
            print(f' You chose {options[3]} {emoji_paper}')
        elif self.user_move == 4:
            print("\n")
            print(f'You chose {options[4]} {emoji_scissors}')
        else:
            print("\n")
            print("\nPlease enter a number between 1 and 4!")


    # Compare user input with CPU and determine a winner of that round
    def round_result(self):

        print("--------------------------------------------------------------\n")
        print (f' CPU chose {options[self.CPU_move]}')
        print("--------------------------------------------------------------\n")

        sleep(0.3)
        if (self.CPU_move == 2 and self.user_move == 3) or (self.CPU_move == 3 and self.user_move == 4) or (self.CPU_move == 4 and self.user_move == 2):
            print(f'User Player won this round {emoji_winner}\n')
            self.winner_player = self.winner_player + 1
        elif (self.CPU_move == 2 and self.user_move == 4) or (self.CPU_move == 3 and self.user_move == 2) or (self.CPU_move == 4 and self.user_move == 3):
            print(f'CPU won this round {emoji_losser}\n')
            self.winner_CPU = self.winner_CPU + 1
        else:
            print(f'( It\'s a tie! {emoji_starface}\n')
            # round is user to count each round and stop the game after 3 rounds
            self.round = self.round + 1


    # TODO: define a function to set the best of 3 games and determine a winner for the game

       # TODO: Show to user each round and partial results of each round (if we have time)

        # Round (#): print emoji_winner
        # Round results: print emoji_winner
        # Parcial results: CPU won (x times) Player won (y times)


    # use the variables Round and winner counter already set in the beginning of the game

    # TODO assign names to the user player? It's a nice to have (if we have time).

    # user input that  overrides the variable user player name

 