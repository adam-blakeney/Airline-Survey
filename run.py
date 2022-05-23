import random

intro_instructions = """ xxxxx """

class GameArea:
    """ this sets the area in which the player and computer will play.
    """
    def __init__(self, name):
        self.name = name
        # Code credit on self.board layout # https://github.com/Damianjacob/MS3-Battleship-Game
        self.board = [
            [" ",  " A", "  B", "  C", "  D", "  E"],
            ["1", "| |", "| |", "| |", "| |", "| |"],
            ["2", "| |", "| |", "| |", "| |", "| |"],
            ["3", "| |", "| |", "| |", "| |", "| |"],
            ["4", "| |", "| |", "| |", "| |", "| |"],
            ["5", "| |", "| |", "| |", "| |", "| |"],
        ]
        self.board_array = np.array(self.board)
        self.computer_displayed_board = np.array(self.board)
        self.user_score = 0
        self.computer_score = 0
        self.column_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}

def user_place_ship(self):
        """
        This function allows the user to place their 3 ships 
        it verfies all the data input by user is correct and if not then sends error message
        it will loop to allow for a re input
        """
        print("Time to place your ships!")
        user_board.display_board()
        added_ship_count = 0
        while added_ship_count < 3:
            while True:
                while True:
                    try:
                        y_input = input("Choose letter (A to E):\n").upper()
                        print('')
                        y_list = ['A', 'B', 'C', 'D', 'E']
                        if y_input not in y_list:
                            raise ValueError(
                                "You must select a letter from A to E!")
                    except ValueError as a:
                        print(f"Invalid data: {a}, please try again.\n")
                        continue
                    else:
                        break
                while True:
                    try:
                        x_input = input("Choose number (1 to 5):\n")
                        print('')
                        x_list = ['1', '2', '3', '4', '5']
                        if x_input not in x_list:
                            raise ValueError(
                                "You must select a number from 1 to 5!")
                    except ValueError as a:
                        print(f"Invalid data: {a}, please try again.\n")
                        continue
                    else:
                        break
                y_input = self.column_map[y_input]
                x_input = int(x_input)
                if self.board_array[x_input, y_input] == '|O|':
                    print("You already have a ship here! Try again!")
                    print('')
                else:
                    break
            self.board_array[x_input, y_input] = '|O|'
            added_ship_count += 1
            user_board.display_board()
            if added_ship_count == 3:
                print('')
                print("Great job placing the ships! Let's start the game!")
                print('')
                # computer_board.randomize_ship_coordinates()
                self.display_board()
                self.display_computer_board()
                # coin_flip(user_board, computer_board)
                play_game()
    
def user_shoot(self):
         """
        Function will allow user to type in coordinates
        to hit.
        it will display if it is a hit or miss.
        it will also verify input is correct
        """
while True:
            print('')
            print("Time to take your shot!")
            print('')
            self.display_computer_board()
            y_coord = self.column_map[self.validate_y_coordinate()]
            x_coord = int(self.validate_x_coordinate())
            if self.board_array[x_coord, y_coord] == '|O|':
                self.computer_displayed_board[x_coord, y_coord] = '|X|'
                self.board_array[x_coord, y_coord] = '|X|'
                print('')
                print('That was a hit! Good job, we can beat them!')
                print('')
                self.user_score += 1
                break
            elif self.computer_displayed_board[x_coord, y_coord] == '|X|':
                print('')
                print("This place has already been hit! Try another..")
            elif self.computer_displayed_board[x_coord, y_coord] == '|-|':
                print('')
                print("This place has already been hit! Try another..")
            else:
                self.computer_displayed_board[x_coord, y_coord] = '|-|'
                print('')
                print("SPLASH... thats a miss.")
                print('')
                break
self.display_computer_board()
if self.user_score < 3:
        user_board.computer_shoot()


def computer_shoot(self):
        """
        This fuction automatically carries out the computers turn 
        and displays the results.
        """
        print('')
        print("Watch out they are firing...")
        while True:
            y_target = random.randint(1, 5)
            x_target = random.randint(1, 5)
            if self.board_array[x_target, y_target] == '|X|':
                continue
            elif self.board_array[x_target, y_target] == '|-|':
                continue
            elif self.board_array[x_target, y_target] == '|O|':
                self.board_array[x_target, y_target] = '|X|'
                print('')
                print('Ouchhh. we have lost a ship..')
                self.computer_score += 1
                print('')
                break
            else:
                self.board_array[x_target, y_target] = '|-|'
                print('')
                print("Phew.. close one")
                print('')
                break
        self.display_board()

def progress_game(self):
        """
        This function will continue in a loop 
        until the player or computer score reaches 3
        """
        while True:
            computer_board.user_shoot()
            if (computer_board.user_score) == 3:
                computer_board.user_wins()
                break
            elif (user_board.computer_score) == 3:
                user_board.computer_wins()
                break
            else:
                pass

def user_wins(self):
 """
This fucntion will be carried out when the user score equals 3
        
"""
    print('')
    print("You did it! I never doubter you sailor! ")
    print("Those pesky water-goers wont be coming back any time soon! ")
    print("To start the battle again click RUN PROGRAM at the top")

def computer_wins(self):
        """
        This fucntion will be carried out when the computer score equals 3
        
        """
    print('')
    print("Oh no... we have lost all our ships.. ")
    print("We have been defeated.. its time to go")
    print("Defeated...")
    print("To start the battle again click RUN PROGRAM at the top")

    # def coin_flip(user_board, computer_board):

def start_game():
        """
    This function is used to call functions which will start the game and set it up
    """
    global user_board
    global computer_board
    user_board = GameBoard("name=user")
    computer_board = GameBoard("name=computer")
    user_board.ask_user_ship_placement()
    computer_board.progress_game()


def introduction():
        """
    Initial message to introduce title of the game.
    Input will appear for user to type in their name.
    While loop will ensure that user does not leave
    the name input empty.
    Paragraph will appear to explain rules of the game
    and ask user if they wish to continue.
    """
    print('-' * 40)
    print("BattleShip")
    print('-' * 40)
    print('')
    print("Welcome to BattleShip the game")
    print(intro_instructions)
    print('')
    print("Get ready they are coming...")
    print('')


    def ask_user_ready():
        """
    This function is written to give the user control over when to start the game.
    it is given by either a 'go' or 'no' response
        """
    while True:
        confirmation_response = input("go or no?\n").lower()

        if confirmation_response == 'go':
            start_game()
            break
        elif confirmation_response == 'no':
            end_game()
            break
        else:
            print('')
            print("You must type either 'go' or 'no'!")
            print('')

    def end_game():
        

    def main():


