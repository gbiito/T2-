def imprime(mat):
    for x in mat:
        print(x)
    print()

def valido(lab, res, f, c):
    if f < 0 or f >= len(lab):
        return False
    if c < 0 or c >= len(lab[0]):
        return False
    if res[f][c] == 1:
        return False
    if lab[f][c] == 0:
        return False
    return True

def laberB(lab, res, f, c, puntos):
    if f == 0 and c == 0:
        if valido(lab, res, f, c):
            puntos_finales = puntos + (lab[f][c] if isinstance(lab[f][c], int) else 0)
            if puntos_finales >= 23:
                res[f][c] = 1
                print(f"¡CAMINO EXITOSO ENCONTRADO CON {puntos_finales} PUNTOS!")
                imprime(res)
                return True
            else:
                return False
        else:
            return False

    if valido(lab, res, f, c):
        res[f][c] = 1
        
        print(f"Movimiento a posición [{f}][{c}] (Puntos actuales: {puntos}):")
        imprime(res)

        puntos_actuales = puntos
        if isinstance(lab[f][c], int) and lab[f][c] in [3, 4]:
            puntos_actuales += lab[f][c]

        if laberB(lab, res, f - 1, c, puntos_actuales):
            return True
        elif laberB(lab, res, f, c + 1, puntos_actuales):
            return True
        elif laberB(lab, res, f + 1, c, puntos_actuales):
            return True
        elif laberB(lab, res, f, c - 1, puntos_actuales):
            return True
        else:
            res[f][c] = 0
            return False
    else:
        return False

lab = [
    ["F", 1, 0, 3, 0, 1, 1, 1, 0],
    [1, 3, 0, 1, 1, 4, 0, 1, 3],
    [1, 0, 1, 1, 0, 1, 1, 0, 1],
    [3, 1, 1, 0, 3, 1, 0, 4, 1],
    [1, 0, 4, 1, 1, 0, 1, 1, 3],
    [1, 1, 0, 1, 3, 1, 4, 0, 1],
    [0, 1, 1, 4, 0, 1, 1, 1, 0],
    [1, 4, 0, 1, 1, 0, 3, 1, 1],
    ["I", 1, 3, 0, 1, 4, 1, 3, 1]
]

res = [[0 for _ in range(9)] for _ in range(9)]

print("=== LABERINTO ORIGINAL ===")
imprime(lab)

if laberB(lab, res, 8, 0, 0):
    print("¡Salimos del laberinto con éxito!")
else:
    print("Quedamos atrapados o ninguna ruta acumuló los 23 puntos mínimos.")