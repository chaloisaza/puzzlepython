# -*- coding: utf-8 -*-

from State import State
from PriorityQueue import PriorityQueue
import time

class Solve:
    def __init__(self, initial_state=None):

        #el array de numeros que llega enviarlo a la clase state
        self.initial_state = State(initial_state)

        #array al que debe llegar pero no de cero a 8 sino de 1 a 0
        self.goal = range(1, 9)

    def _rebuildPath(self, end):
        path = [end]
        state = end.parent
        while state.parent:
            path.append(state)
            state = state.parent
        return path

    def solve(self):
        openset = PriorityQueue()
        openset.add(self.initial_state)
        closed = set()
        moves = 0
        print('Resolviendo puzzle...')
        start = time.time()
        while openset:
            current = openset.poll()
            if current.values[:-1] == self.goal:
                end = time.time()
                print('Se encontró una solución:')
                path = self._rebuildPath(current)
                for state in reversed(path):
                    print(state)
                    print
                print('Resuelto con %d movimentos' % len(path))
                print('Se encontró una solución en %2.f segundos' %
                      float(end - start))
                break
            moves += 1
            for state in current.possible_moves(moves):
                if state not in closed:
                    openset.add(state)
            closed.add(current)
        else:
            openset
            end = time.time()
            print('¡No se consiguió solucionar!', float(end - start))
