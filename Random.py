from Player import Player
import random


class Random(Player):

    def __init__(self, board, player):
        Player.__init__(self, board, player)

    def move(self):
        if self.board.finished_game():
            return False

        row = random.randint(0, 2)
        col = random.randint(0, 2)
        while not (self.board.valid_move(row, col)):
            row = random.randint(0, 2)
            col = random.randint(0, 2)
        self.board.move(row, col, self.player)

        return True
