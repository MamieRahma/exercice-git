import random

# ==============================
# Création d'une matrice 2D aléatoire
# ==============================
def creer_tableau(lignes, colonnes):
    """
    Génère une matrice 2D avec des valeurs aléatoires
    """
    return [[random.randint(1, 100) for _ in range(colonnes)] for _ in range(lignes)]


# ==============================
# TRI A BULLE
# ==============================
def tri_bulle(tab):
    """
    Principe :
    On compare les éléments deux à deux et on échange si mal ordonné.
    On répète jusqu'à ce que tout soit trié.
    """
    for ligne in tab:
        n = len(ligne)
        for i in range(n):
            for j in range(0, n - i - 1):
                if ligne[j] > ligne[j + 1]:
                    ligne[j], ligne[j + 1] = ligne[j + 1], ligne[j]
    return tab


# ==============================
# TRI PAR SELECTION
# ==============================
def tri_selection(tab):
    """
    Principe :
    On cherche le plus petit élément et on le met au début.
    Puis on recommence pour le reste.
    """
    for ligne in tab:
        n = len(ligne)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if ligne[j] < ligne[min_idx]:
                    min_idx = j
            ligne[i], ligne[min_idx] = ligne[min_idx], ligne[i]
    return tab


# ==============================
# TRI PAR INSERTION
# ==============================
def tri_insertion(tab):
    """
    Principe :
    On prend un élément et on l'insère à la bonne position.
    """
    for ligne in tab:
        for i in range(1, len(ligne)):
            key = ligne[i]
            j = i - 1
            while j >= 0 and ligne[j] > key:
                ligne[j + 1] = ligne[j]
                j -= 1
            ligne[j + 1] = key
    return tab


# ==============================
# TRI RAPIDE (QuickSort)
# ==============================
def tri_rapide_liste(liste):
    if len(liste) <= 1:
        return liste
    pivot = liste[0]
    gauche = [x for x in liste[1:] if x <= pivot]
    droite = [x for x in liste[1:] if x > pivot]
    return tri_rapide_liste(gauche) + [pivot] + tri_rapide_liste(droite)


def tri_rapide(tab):
    """
    Principe :
    On choisit un pivot, on sépare les petits et les grands,
    puis on trie récursivement.
    """
    return [tri_rapide_liste(ligne) for ligne in tab]


# ==============================
# TRI PAR FUSION
# ==============================
def fusion(gauche, droite):
    resultat = []
    i = j = 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    resultat += gauche[i:]
    resultat += droite[j:]
    return resultat


def tri_fusion_liste(liste):
    if len(liste) <= 1:
        return liste
    milieu = len(liste) // 2
    gauche = tri_fusion_liste(liste[:milieu])
    droite = tri_fusion_liste(liste[milieu:])
    return fusion(gauche, droite)


def tri_fusion(tab):
    """
    Principe :
    On divise la liste en deux, on trie puis on fusionne.
    """
    return [tri_fusion_liste(ligne) for ligne in tab]


# ==============================
# RECHERCHE LINEAIRE
# ==============================
def recherche_lineaire(tab, valeur):
    """
    Parcourt toute la matrice jusqu'à trouver la valeur
    """
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == valeur:
                return (i, j)
    return None


# ==============================
# RECHERCHE BINAIRE
# ==============================
def recherche_binaire(liste, valeur):
    """
    Fonctionne seulement si la liste est triée
    """
    debut = 0
    fin = len(liste) - 1

    while debut <= fin:
        milieu = (debut + fin) // 2
        if liste[milieu] == valeur:
            return milieu
        elif liste[milieu] < valeur:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1


# ==============================
# RECHERCHE DICHOTOMIQUE (même principe)
# ==============================
def recherche_dichotomie(liste, valeur):
    return recherche_binaire(liste, valeur)
