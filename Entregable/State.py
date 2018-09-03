# -*- coding: utf-8 -*-

class State:
    def __init__(self, values, moves=0, parent=None):
        self.values = values
        self.moves = moves
        self.parent = parent
        self.goal = range(1, 9)

    def possible_moves(self, moves):
        i = self.values.index(0)
        if i in [3, 4, 5, 6, 7, 8]:
            new_board = self.values[:]
            new_board[i], new_board[i - 3] = new_board[i - 3], new_board[i]
            yield State(new_board, moves, self)
        if i in [1, 2, 4, 5, 7, 8]:
            new_board = self.values[:]
            new_board[i], new_board[i - 1] = new_board[i - 1], new_board[i]
            yield State(new_board, moves, self)
        if i in [0, 1, 3, 4, 6, 7]:
            new_board = self.values[:]
            new_board[i], new_board[i + 1] = new_board[i + 1], new_board[i]
            yield State(new_board, moves, self)
        if i in [0, 1, 2, 3, 4, 5]:
            new_board = self.values[:]
            new_board[i], new_board[i + 3] = new_board[i + 3], new_board[i]
            yield State(new_board, moves, self)

    def score(self):
        return self._h() + self._g()

    def _h(self):
        return sum([1 if self.values[i] != self.goal[i] else 0 for i in range(8)])

    def _g(self):
        return self.moves

    def __cmp__(self, other):
        return self.values == other.values

    def __eq__(self, other):
        return self.__cmp__(other)

    def __hash__(self):
        return hash(str(self.values))

    def __lt__(self, other):
        return self.score() < other.score()

    def __str__(self):
        return '\n'.join([str(self.values[:3]),
                          str(self.values[3:6]),
                          str(self.values[6:9])]).replace('[', '').replace(']', '').replace(',', '').replace('0', 'x')
