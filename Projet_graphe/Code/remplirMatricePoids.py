import streamlit as st
from math import inf

def remplirMatriceNonOrinte():
    n = st.number_input("Veuillez entrer le nombre de sommets de votre graphe, s'il vous plaît:", step=1)

    # Convert to integer
    n = int(n)

    # Text area for entering the matrix
    matrix_input = st.text_area("Veuillez entrer la matrice de poids (séparée par des espaces ou des retours à la ligne)")

    # Process the input and create the matrix
    M = [[inf] * n for _ in range(n)]
    rows = matrix_input.split('\n')
    for i, row in enumerate(rows):
        elements = row.split()
        for j, e in enumerate(elements):
            
                M[i][j] = int(e)

    st.write("\nvotre matrice de poids est : ")
    for i in range(n):
        st.write(f"{i + 1} =", M[i])

    return M
def remplirMatriceOriente():
    n = st.number_input("Veuillez entrer le nombre de sommets de votre graphe, s'il vous plaît:", step=1)

    # Convert to integer
    n = int(n)

    # Text area for entering the matrix
    matrix_input = st.text_area("Veuillez entrer la matrice de poids (séparée par des espaces ou des retours à la ligne)")

    # Process the input and create the matrix
    M = [[inf] * n for _ in range(n)]
    rows = matrix_input.split('\n')
    for i, row in enumerate(rows):
        elements = row.split()
        for j, e in enumerate(elements):
            
                M[i][j] = int(e)


    # Display the matrix
    st.write("\nVotre matrice de poids est :")
    for i in range(n):
        st.write(f"Sommet {i + 1} =", M[i])

    return M


def remlplirprOrd() :
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
            if e == "inf" or e == "INF":
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

    return M