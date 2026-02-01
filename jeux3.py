import tkinter as tk

class JeuDePoints:
    def __init__(self, root):
        self.root = root
        # Configuration du tableau (Matrice)
        self.lignes, self.colonnes = 15, 12 
        self.gap, self.marge = 40, 40
        
        # Initialisation du tableau avec des 0 (0 = vide)
        self.grille = [[0 for _ in range(self.colonnes)] for _ in range(self.lignes)]
        
        self.joueur, self.scores = 1, {1: 0, 2: 0} # 1=Rouge, 2=Bleu
        self.couleurs = {1: "red", 2: "blue"}

        self.label = tk.Label(root, text="Tour : Rouge", font=("Arial", 14), fg="red")
        self.label.pack()

        self.can = tk.Canvas(root, width=self.colonnes*self.gap + 40, height=self.lignes*self.gap + 40, bg="white")
        self.can.pack()
        
        self.dessiner_feuille()
        self.can.bind("<Button-1>", self.clic)

    def dessiner_feuille(self):
        for l in range(self.lignes):
            y = l * self.gap + self.marge
            self.can.create_line(0, y, 800, y, fill="#e0ebff")
        for c in range(self.colonnes):
            x = c * self.gap + self.marge
            self.can.create_line(x, 0, x, 800, fill="#e0ebff")

    def clic(self, e):
        # Conversion pixels -> indices du tableau
        c = round((e.x - self.marge) / self.gap)
        l = round((e.y - self.marge) / self.gap)

        # Vérification des limites du tableau et si la case est vide (0)
        if 0 <= l < self.lignes and 0 <= c < self.colonnes:
            if self.grille[l][c] == 0:
                self.grille[l][c] = self.joueur # On remplit la case du tableau
                
                # Dessin
                x, y = c * self.gap + self.marge, l * self.gap + self.marge
                self.can.create_oval(x-7, y-7, x+7, y+7, fill=self.couleurs[self.joueur])
                
                if not self.verifier_carre(l, c):
                    self.joueur = 2 if self.joueur == 1 else 1
                
                self.maj_ui()

    def verifier_carre(self, l, c):
        carre_cree = False
        # On teste les 4 carrés dont (l, c) peut être un sommet
        for dl, dc in [(-1, -1), (-1, 0), (0, -1), (0, 0)]:
            # Vérifier si on ne sort pas du tableau
            if 0 <= l+dl < self.lignes-1 and 0 <= c+dc < self.colonnes-1:
                # Accès direct au tableau pour les 4 coins
                if (self.grille[l+dl][c+dc] == self.joueur and
                    self.grille[l+dl+1][c+dc] == self.joueur and
                    self.grille[l+dl][c+dc+1] == self.joueur and
                    self.grille[l+dl+1][c+dc+1] == self.joueur):
                    
                    self.scores[self.joueur] += 1
                    x0, y0 = (c+dc)*self.gap+self.marge, (l+dl)*self.gap+self.marge
                    self.can.create_rectangle(x0, y0, x0+self.gap, y0+self.gap, fill=self.couleurs[self.joueur], stipple="gray25")
                    carre_cree = True
        return carre_cree

    def maj_ui(self):
        c = self.couleurs[self.joueur]
        self.label.config(text=f"Rouge: {self.scores[1]} | Bleu: {self.scores[2]}", fg=c)

if __name__ == "__main__":
    root = tk.Tk()
    JeuDePoints(root)
    root.mainloop()
