#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import print_function #try to delete print error but we are in 3.7 and it's not logical import from future...
import random
from Solve import Solve

# creaar un array entre 0 y 8 y hacerlo random
puzzle = list(range(9))
random.shuffle(puzzle)
print("Arreglo a resolver: ",puzzle)
# enviar ese array a clase Solve
solution = Solve(puzzle)

# solution
solution.solve()
