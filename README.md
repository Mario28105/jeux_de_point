# jeux_de_point
1. La Création du Tableau (La Matrice)
self.lignes, self.colonnes = 15, 12 : On définit une taille fixe pour notre feuille de papier. Contrairement au dictionnaire, ici le "cahier" a des bords bien définis.

self.grille = [[0 for _ in range(self.colonnes)] for _ in range(self.lignes)] :

C'est une liste de listes.

On la remplit de 0 pour dire que chaque intersection est "vide" au départ.

Si un joueur Rouge clique, on mettra un 1. Si c'est le Bleu, un 2.

2. Le Dessin et les Pixels
c = round((e.x - self.marge) / self.gap) :

e.x est la position de ta souris en pixels.

On transforme ces pixels en un indice de colonne pour notre tableau. Si tu cliques à 80px et que le gap est de 40px, c vaudra 2.

if 0 <= l < self.lignes and 0 <= c < self.colonnes: :

C'est la sécurité. Comme le tableau a une taille fixe, si tu cliques en dehors (ex: à l'indice 20 alors qu'il n'y a que 12 colonnes), le programme s'arrêterait avec une erreur. Cette ligne vérifie que le clic est bien "sur la feuille".

3. La Logique de Jeu
if self.grille[l][c] == 0: : On vérifie dans la matrice si la case est vide avant de poser un point. C'est beaucoup plus rapide que de chercher dans une liste.

self.grille[l][c] = self.joueur : On enregistre l'action du joueur dans la mémoire de l'ordinateur (la matrice).

4. La Vérification des Carrés (Mathématiques)
for dl, dc in [(-1, -1), (-1, 0), (0, -1), (0, 0)]: :

Un point peut être n'importe quel sommet d'un carré (en haut à gauche, en bas à droite, etc.).

dl (delta ligne) et dc (delta colonne) représentent ces 4 directions possibles pour trouver le "coin de départ" du carré.

if (self.grille[l+dl][c+dc] == self.joueur and ...) :

Ici, on accède directement aux voisins dans la matrice.

On regarde si la case [l][c], sa voisine de droite [l][c+1], sa voisine du bas [l+1][c] et sa diagonale [l+1][c+1] contiennent toutes le même numéro de joueur.

5. Mise à jour de l'Interface
self.label.config(...) : On modifie le texte en haut pour afficher les scores stockés dans self.scores.

stipple="gray25" : Dans create_rectangle, cela permet de ne pas masquer totalement les lignes bleues du cahier, en créant un effet de remplissage par petits points (tramage).