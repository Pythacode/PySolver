# ------------------------------------------------------------------------------------- #
# ----------------------- Pythacode © Tous droits réservés 2025 ----------------------- #
# ------------------------------------------------------------------------------------- #

from decimal import Decimal

try :
    import re
except ModuleNotFoundError :
    print("[31mVeulliez installer le module re avec \"pip install re2\"[39m") # Affiche un message d'érreur en cas de module non instalé. Les caractère au début et à la fin sont des code couleur : "Rouge" & "Reset" (Remet les couleurs de bases) 
    exit(1) # Fini le programe avec le code d'érreur 1

def contient_nombre(chaine):
    return bool(re.search(r'\d', chaine)) # Vérifie si chaine contient un chiffre

def split_with_sign(text, sign:str) :
    if isinstance(text, str) : # Vérifie si il s'agit d'une chaine de texte
        text = text.split(sign) # Sépare la chaine par sign
        for i in range(len(text)) : # Liste tous les élèment de la chaine
            i -= 1
            car = text[i]
            if car != '' : # Vérifie que ce n'est pas un élèment vide
                if not car[0] in ["+", "-"] : # Cherche si l'expression a déjà un signe
                    text[i] = sign + car # Si non, on ajoute le signe
            else :
                text.remove(car) # Suprime l'élèment vide
        return text
    else : # Si c'est une liste
        result = []
        for i in text : 
            result = result + split_with_sign(i, sign) # Appele la fonction pour tous les élèment de la liste, et ajoute les résultat à une liste de résultat
        return result

def get_param(exp, is_invert=False) :
    
    """
    Cette fonction permet de trouver les paramètres a, b, c, d, e, f pour résoudre le système. Pour ce faire,
        On Récupère une liste sous forme (par exemple) de ["+2x", "-7x", "-8", "+x", ...]
        On boucle cette liste, puis :
            Si l'élèment contient un y :
                Si il y à un chiffre dans l'élèment sans le y, alors, on ajoute se chiffre a la liste y (en le convertisant en float)
                Sinon, on ajoute 1 ou -1 en fonction du signe (élèments seras alors égal à "-y" ou "+y")
            Idem avec x
            Sinon, on ajoute l'élèment à r (en le convertisant en float)
        Ensuite,
        Si la variable is_invert = True :
            On inverse tous les élèments de chaque liste.
            Cela permet de mettre tous les élèment dans le menbre gauche de l'équation, la variable is_invert seras donc égal à true quand se seras le membre droit de l'équation
        Enfin, on fait la somme des liste, puis on les renvoie.
    """
    
    exp = split_with_sign(exp, "+") # Obtient une liste des élèments (x, y, r) en séparant par un plus
    exp = split_with_sign(exp, "-") # Obtient une liste des élèments (x, y, r) en séparant par un moin

    x = []
    y = []
    r = []

    for element in exp : # Boucle les élèments
        if "y" in element :
            element = element.replace('y', '')
            if contient_nombre(element) :
                y.append(float(element))
            elif element.startswith('+') :
                y.append(1)
            elif element.startswith('-') :
                y.append(-1)
        elif "x" in element :
            element = element.replace('x', '')
            if contient_nombre(element) :
                x.append(float(element))
            elif element.startswith('+') :
                x.append(1)
            elif element.startswith('-') :
                x.append(-1)
        else :
            r.append(float(element))

    
    if is_invert :
        x = [-i for i in x]
        y = [-i for i in y]
        r = [-i for i in r]

    x = [Decimal(i) for i in x ]
    y = [Decimal(i) for i in y ]
    r = [Decimal(i) for i in r ]

    x = (sum(x))
    y = (sum(y))
    r = (sum(r))


    return x, y, r

def resoudre_systeme(a, b, c, d, e, f) : # Algoritme pour résoudre le système. Complexité : O(n*m) (Pour une matrice de taille (n, m))
    
    """
    Pour l'équation suivante :
        | ax+by=e
        | cx+dy=f
    """

    def entier_matrice(entier, matrice : list[list]) : # Multiplie un flotant (entier) par une matrice (matrice)
        for y, line in enumerate(matrice) : # Boucle tous les coeficient de la matrice
            for x, row in enumerate(line) :
                matrice[y][x] = entier * row # Les multiplie par "entier"

        return matrice # Retourne la matrice

    def matrice22_matrice21(matrice22 : list[list], matrice21 : list[list]) : # Multiplie une matrice de taille (2, 2) par une matrice de taille (2, 1)
        return float(matrice22[0][0]*matrice21[0][0]+matrice22[0][1]*matrice21[1][0]), float(matrice22[1][0]*matrice21[0][0]+matrice22[1][1]*matrice21[1][0])

    matrice = [
        [a, b],
        [c, d]
    ]

    matrice_result = [
        [e],
        [f]
    ]

    det = 1/(matrice[0][0] * matrice[1][1] - matrice[1][0] * matrice[0][1]) # Calcule le determinant

    matrice_pre_inversed = [
        [matrice[1][1], -matrice[0][1]],
        [-matrice[1][0], matrice[0][0]]
    ] # Pré-inverse la matrice

    return matrice22_matrice21(entier_matrice(det, matrice_pre_inversed), matrice_result) # Retourne la résolution de l'équation

print('Les inconus doivent être x & y')

exp1 = input('Entrer une expression : ').replace(' ', '') # Demande la première expression, et suprime les espaces
exp2 = input('Entrer une expression : ').replace(' ', '') # Idem pour la deuxième expression

a, b, e = get_param(exp1.split("=")[0]) # On récupère les paramètre (Nombre de x, de y et de r) pour le membre gauche de l'équation
param = get_param(exp1.split("=")[1], True) # On récupère les paramètre (Nombre de x, de y et de r) pour le membre droit de l'équation (qui seront mis dans le membre gauche graca è is_inverted)
a, b, e = a+param[0], b+param[1], e+param[2] # On ajoute les parametre du membre droit à ceux du membre gauche
e = -e # On inverse r (Pour le mettre dans le membre de droite)

# Idem
c, d, f = get_param(exp2.split("=")[0])
param = get_param(exp2.split("=")[1], True)
c, d, f = c+param[0], d+param[1], f+param[2]
f = -f

x, y = resoudre_systeme(a, b, c, d, e, f)

print(f"Résultat :\n\tx = {x},\n\ty = {y}")

# ------------------------------------------------------------------------------------- #
# ----------------------- Pythacode © Tous droits réservés 2025 ----------------------- #
# ------------------------------------------------------------------------------------- #