# -*- coding: utf-8 -*-
from __future__ import print_function #tratar de eliminar error
from random import shuffle
from Solve import Solve

# creaar un array entre 0 y 8 y hacerlo random
puzzle = range(9)
shuffle(puzzle)
print("Arreglo a resolver: ",[0, 2, 5, 3, 1, 7, 8, 4, 6])
# enviar ese array a clase Solve
solution = Solve(puzzle)

# solution
solution.solve()
