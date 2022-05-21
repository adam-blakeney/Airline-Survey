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

def player_hide():
    """
    this lets the player choose where they want to hide.
    this will return an error if the input is not correct
    """
