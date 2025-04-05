import streamlit as st
from djikstra import djikstra
from bellman import Bellman
from remplirMatricePoids import remplirMatriceOriente
from remplirMatricePoids import remplirMatriceNonOrinte

import remplirMatricePoids, bellman
from math import inf

def main():
    st.title("Graphe & Application")

    menu_choices = [
        "Display",
        "Djikstra",
        "Bellman",
        #"Prim",
        #"Problème d'ordonnancement",
    ]

    choix = st.selectbox("Veuillez choisir votre algorithme préféré s'il vous plaît:", menu_choices)

    if choix == "Display":
        display_matrix()
    elif choix == "Djikstra":
        run_djikstra()
    elif choix == "Bellman":
        run_bellman()
    elif choix == "Problème d'ordonnancement":
        run_scheduling()

def display_matrix():
    g = st.radio("Choisissez le type de graphe:", ["Graphe orienté", "Graphe non orienté"])
    if g == "Graphe orienté":
        M = remplirMatricePoids.remplirMatriceOriente()
        st.table(M)
    else:
        M = remplirMatricePoids.remplirMatriceNonOrinte()
        st.table(M)

def run_djikstra():
    M = remplirMatricePoids.remplirMatriceOriente()

    # Check for negative weights
    if any(any(weight < 0 for weight in row) for row in M):
        st.write("Le graphe contient des poids négatifs. Veuillez entrer des poids non négatifs.")
        return

    s = st.slider("Veuillez choisir la source s'il vous plaît:", 1, len(M), 1)

    M_Dis = djikstra(M, s)
    st.write("\nDistance depuis la source (Dijikstra):")
    for i, distance in enumerate(M_Dis):
        st.write(f"Sommet {s} ------------> Sommet {i+1}: {distance}")
    
    # Force a rerun of the app to update the UI
    st.experimental_rerun()


def run_bellman():
    M = remplirMatricePoids.remplirMatriceOriente()
    s = st.slider("Veuillez choisir la source s'il vous plaît:", 1, len(M), 1)
    
    # Call Bellman function
    M_Dis = bellman.Bellman(M, s)
    
    # Check for negative cycle
    if M_Dis is None:
        st.write("Le graphe contient un cycle négatif.")
    else:
        st.write("\nDistance depuis la source (Bellman):")
        for i, distance in enumerate(M_Dis):
            st.write(f"Sommet {s} ------------> Sommet {i+1}: {distance}")
    
    # Force a rerun of the app to update the UI
    st.experimental_rerun()

def run_scheduling():
    M = remplirMatricePoids.remlplirprOrd()
    M_Dis = bellman.Bellman(M)
    st.write("\nDistance depuis la source (Problème d'ordonnancement):")
    for i, distance in enumerate(M_Dis):
        st.write(f"Sommet {i+1} ------------> {(-1)*distance}")
    
    # Force a rerun of the app to update the UI
    st.experimental_rerun()

if __name__ == "__main__":
    main()
