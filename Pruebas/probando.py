#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 16:06:40 2018

@author: macbookduvan
"""

# Puzle lineal con busqueda en profundidad
from arbol import Nodo


def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        # Esta es la diferencia con BFS
        nodo = nodos_frontera.pop()
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            # Solucion encontrada
            solucionado = True
            return nodo
        else:
            # Expandir nodos hijos
            dato_nodo = nodo.get_datos()

            # Operador izquierdo
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2],
                    dato_nodo[3], dato_nodo[4], dato_nodo[5], dato_nodo[6]]
            hijo_izquierdo = Nodo(hijo)
            if not hijo_izquierdo.en_lista(nodos_visitados) \
                    and not hijo_izquierdo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo)

            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1],
                    dato_nodo[3], dato_nodo[4], dato_nodo[5], dato_nodo[6]]
            hijo_izquierdo2 = Nodo(hijo)
            if not hijo_izquierdo2.en_lista(nodos_visitados) \
                    and not hijo_izquierdo2.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo2)

            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3],
                    dato_nodo[2], dato_nodo[4], dato_nodo[5], dato_nodo[6]]
            hijo_izquierdo3 = Nodo(hijo)
            if not hijo_izquierdo3.en_lista(nodos_visitados) \
                    and not hijo_izquierdo3.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo3)

            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[2],
                    dato_nodo[4], dato_nodo[3], dato_nodo[5], dato_nodo[6]]
            hijo_izquierdo4 = Nodo(hijo)
            if not hijo_izquierdo4.en_lista(nodos_visitados) \
                    and not hijo_izquierdo4.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo4)

            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[2],
                    dato_nodo[3], dato_nodo[5], dato_nodo[4], dato_nodo[6]]
            hijo_izquierdo5 = Nodo(hijo)
            if not hijo_izquierdo5.en_lista(nodos_visitados) \
                    and not hijo_izquierdo5.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo5)

            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[2],
                    dato_nodo[3], dato_nodo[4], dato_nodo[6], dato_nodo[5]]
            hijo_izquierdo6 = Nodo(hijo)
            if not hijo_izquierdo6.en_lista(nodos_visitados) \
                    and not hijo_izquierdo6.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo6)

#            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[2], dato_nodo[3], dato_nodo[4], dato_nodo[5], dato_nodo[7],dato_nodo[6]]
#            hijo_izquierdo7 = Nodo(hijo)
#            if not hijo_izquierdo7.en_lista(nodos_visitados) \
#                and not hijo_izquierdo7.en_lista(nodos_frontera):
#                nodos_frontera.append(hijo_izquierdo7)

            nodo.set_hijos([hijo_izquierdo, hijo_izquierdo2, hijo_izquierdo3,
                            hijo_izquierdo4, hijo_izquierdo5, hijo_izquierdo6])


def main():
    estado_inicial = [3, 5, 0, 2, 1, 4, 6]
    solucion = [1, 2, 3, 4, 5, 6, 0]
    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)
    # Mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)


if __name__ == '__main__':
    main()