from Player import Player


class Board:

    def __init__(self):
        self.empty = " "
        self.board = self.__create_board()

    def __create_board(self):
        lst = [[], [], []]
        for row in range(3):
            for col in range(3):
                self.board[row][col].append(self.empty)
        return lst

    def next_player(self):
        return

    def valid_move(self, row, col):
        if 0 <= row <= 2 and 0 <= col <= 2:
            return self.board[row][col] == self.empty
        return False

    def move(self, row, col, player):
        if self.valid_move(row, col):
            self.board[row][col] = player
            return True
        return False

    def check_win(self):
        return

    def finished_game(self):
        for row in self.board:
            for col in row:
                if col == self.empty:
                    return False
        return True

    def __str__(self):
        return
