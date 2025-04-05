from math import inf


n = int(input("donnez le nombre de sommets : \n"))

# Matrice de poids M
print("vous allez introduire votre matrice de poids\n")
M = [[inf] * (n) for i in range(n)]
print("Inisialisation de la matrice de poids \n")
print("M=", M)
for i in range(n):
    for j in range(n):
        e = input(
            "\ndonnez l'élément[" + str(i + 1) +
            "][" + str(j + 1) + "] de la matrice "
        )
        if e == "0":
            M[i][j] = inf
        else:
            M[i][j] = int(e)

for i in range(n):
    for j in range(n):
        M[i][i] = 0

# print("\n")
print("\nvotre matrice de poids est : ")
for i in range(n):
    print((i + 1), "=", M[i])

for i in range(len(M)):
    for j in range(len(M)):
        if M[i][j] != inf:
            M[i][j] = (-1)*M[i][j]


def Bellman(Matrice):
    Distance = [inf]*len(Matrice)
    Distance[0] = 0

    for i in range(len(Matrice)-1):
        for j in range(len(Matrice)):
            for k in range(len(Matrice)):
                if Distance[j] + Matrice[j][k] < Distance[k]:
                    Distance[k] = Distance[j] + Matrice[j][k]

    for i in range(len(Matrice)):
        for j in range(len(Matrice)):
            if Distance[i] + Matrice[i][j] < Distance[j]:
                print("Le graphe contient un cycle négatif")
                return

    return Distance


M_D = Bellman(M)
print("Distance depuis la source")
for i in range(len(M_D)):
    print("Sommet", (i+1), "\t------------>\t", (-1)*M_D[i])
