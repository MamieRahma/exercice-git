import tri_recherche as tr

# Création d'une matrice
tableau = tr.creer_tableau(3, 5)

print("Tableau initial :")
print(tableau)

# Tri
print("\nTri à bulle :")
print(tr.tri_bulle([ligne[:] for ligne in tableau]))

# Recherche
val = tableau[0][0]
print("\nRecherche linéaire de", val)
print(tr.recherche_lineaire(tableau, val))
