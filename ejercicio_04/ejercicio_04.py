"""
Ejercicio 4. Buscar un código en un catálogo ordenado

Un catálogo contiene códigos numéricos ordenados de menor a mayor. Implementa
una búsqueda binaria recursiva para localizar un código.

    def buscar_codigo(codigos, objetivo, izquierda, derecha):
        pass

La función devuelve el índice del código si se encuentra, o -1 si no se
encuentra. Si hay códigos repetidos, puedes devolver el índice de cualquiera de
sus apariciones.

Ejemplos

    codigos = [101, 205, 310, 415, 520, 630, 740]

    buscar_codigo(codigos, 520, 0, len(codigos) - 1)   # 4
    buscar_codigo(codigos, 300, 0, len(codigos) - 1)   # -1
    buscar_codigo([], 300, 0, -1)                      # -1
    buscar_codigo([205], 205, 0, 0)                    # 0

Restricciones

- La solución debe ser recursiva.
- No utilices ciclos ni cortes.
- No busques con objetivo in codigos ni con .index().
- No ordenes la lista dentro de la función: se recibe ordenada.
- En cada llamada, continúa únicamente en la región que todavía pueda contener
  el objetivo.
"""


def buscar_codigo(codigos, objetivo, izquierda, derecha):
    """Busca un código en un catálogo ordenado de menor a mayor."""
    if izquierda > derecha:
        return -1
    medio = (izquierda + derecha) // 2
    if codigos[medio] == objetivo:
        return medio
    elif codigos[medio] < objetivo:
        return buscar_codigo(codigos, objetivo, medio + 1, derecha)
    else:
        return buscar_codigo(codigos, objetivo, izquierda, medio - 1)

# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Cuáles son las dos situaciones en las que termina la búsqueda?
#   se encuentra el codigo, no s encuentra el codigo
#
# 2. ¿Por qué no debes incluir nuevamente la posición central en el
#    siguiente intervalo?
#   porque ya pase por ella y no es lo que buscaba
#
# 3. Completa la traza buscando 300 en codigos. Si una llamada no llega a
#    calcular el medio, escribe "—".
#
#    Llamada | Izquierda | Derecha | Medio | Decisión
#    --------|-----------|---------|-------|---------
#       1    |      0     |    7    |   3   |  Buscar en la mitad
#       2    |      4     |    7    |   5   |  Buscar en la mitad
#       3    |      4     |    4    |   4   |  Encontrado
#       4    |      5     |    4    |   —   |  No encontrado
#
# 4. ¿Qué diferencia hay entre el progreso de esta función y el de
#    contar_desde_limite()?
#       en la búsqueda binaria, se divide el espacio de búsqueda a la mitad en cada llamada,
#       mientras que en contar_desde_limite, se recorre secuencialmente.
#


if __name__ == "__main__":
    codigos = [101, 205, 300, 310, 415, 520, 630, 740]

    print(buscar_codigo(codigos, 520, 0, len(codigos) - 1))   # 4
    print(buscar_codigo(codigos, 300, 0, len(codigos) - 1))   # -1
    print(buscar_codigo([], 300, 0, -1))                      # -1
    print(buscar_codigo([205], 205, 0, 0))                    # 0
