"""
@author: Nouzouhati ATHOUMANI AHAMADA
"""

import turtle
import random

# Configuration de l'écran
ecran = turtle.Screen()
ecran.bgcolor("white")

# Configuration de la tortue
artiste = turtle.Turtle()
artiste.speed(0)
artiste.width(2)

# Liste des couleurs possibles
couleurs = ["red", "blue", "green", "yellow", "purple", "orange"]

# Dessin de motifs aléatoires
for _ in range(100):
    artiste.color(random.choice(couleurs))
    artiste.forward(random.randint(50, 200))
    artiste.right(random.randint(20, 160))

# Terminer le dessin
turtle.done()

