from math import inf

def Bellman(Matrice, start_vertex):
    n = len(Matrice)
    Distance = [inf] * n
    Distance[start_vertex - 1] = 0

    for i in range(n - 1):
        for j in range(n):
            for k in range(n):
                if Matrice[j][k] != 0 and Distance[j] + Matrice[j][k] < Distance[k]:
                    Distance[k] = Distance[j] + Matrice[j][k]

    # Check for negative cycles
    for j in range(n):
        for k in range(n):
            if Matrice[j][k] != 0 and Distance[j] + Matrice[j][k] < Distance[k]:
                return None  # Negative cycle detected

    return Distance
