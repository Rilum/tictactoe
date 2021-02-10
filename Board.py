class Board:

    def __init__(self):
        self.board = [[], [], []]
        create_board(self.board)


def create_board(lst):
    for row in range(3):
        for col in range(3):
            lst[row][col].append(" ")
