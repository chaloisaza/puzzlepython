# -*- coding: utf-8 -*-
from random import shuffle
from Solve import Solve


# creaar un array entre 0 y 8 y hacerlo random
puzzle = range(9)
shuffle(puzzle)
print('Arreglo a resolver: ', puzzle)
# enviar ese array a clase Solve
solution = Solve(puzzle)

# ojo
solution.solve()
