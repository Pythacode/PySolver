# $\textsf{\color{#ba1ce6}{Py}} \textsf {Solver}$

## Sommaire

- Présentation du projet
- Installation
- Utilisation
- Explication du code

## Présentation du projet

> [!WARNING]
> Ce projet n'est en aucun cas certifié infaillible, il peut donc contenir des bugs... Merci de votre compréhension.
> Si vous en trouvez un, vous pouvez me le faire parvenir en [créant une issue](https://github.com/Pythacode/PySolver/issues), **avec la sortie console**

Ce projet a été créé dans le cadre de cours de math.
Il s'agit d'un code en ligne de commande permettant de résoudre un système d'équations à deux inconnues (`x` & `y`) et à deux lignes. Attention, ce programme ne peut pas faire de produit.

## Installation

Pour installer le projet, téléchargez-le avec 
```cmd
git clone https://github.com/Pythacode/PySolver.git
```
ou avec le fichier zip.

Ensuite, rentrez dans le dossier du projet, puis installez les dépendances avec
```cmd
pip install -r requirements.txt
```

> [!TIP]
> Python doit être installé, sinon, [installez-le](https://www.python.org/downloads/).
> Pip doit également être installé, sinon, [installez-le](https://pip.pypa.io/en/stable/installation/) ou ajoutez `python -m` au début de la commande.

## Utilisation 

Pour utiliser le programme, il faut le lancer dans un terminal avec
```cmd
python main.py
```
ou
```cmd
python3 main.py
```

Le programme vous demandera d'entrer les deux expressions l'une après l'autre.

> [!IMPORTANT]
> Veillez à utiliser uniquement `x` et `y` pour les inconnues, et `+`, `-`, `=` pour les signes. Ce programme ne peut pas faire de produit.

## Explication du code

Pour tous ceux & celles qui veulent améliorer le code, le modifier, ajouter une UI, cette section est faite pour toi :

### Fichier `main.py`

> [!TIP]
> Souvent, le code est commenté ligne par ligne dans le fichier. Si tu ne comprends pas cette explication, lis le code, tu comprendras peut-être mieux

#### Fonction `contient_nombre(nbr)`

Cette fonction vérifie si `nbr` contient un nombre.

##### Input :
| Variable | Description | Type | Exemple |
|----------|----|--|---------|
| nbr  | Variable à vérifier si elle contient un nombre | str  | "4x" ou "x"  |

##### Output :
bool :
`True` si `nbr` contient un nombre

### Fonction `split_with_sign(text, sign:str)`

Permet de séparer `text` avec `sign` en gardant le signe, si l'expression n'en a pas déjà (`+` ou `-`)

##### Input :
| Variable | Description | Type | Exemple |
|----------|----|--|---------|
| text  | Variable à séparer | str  | "4x+9y" |
| sign  | Signe pour séparer | str  | "+" |

##### Output :
Une liste.

### Fonction `get_param(exp, is_invert=False)`

Cette fonction permet de trouver les paramètres a, b, c, d, e, f pour résoudre le système.

##### Input :
| Variable | Description | Type | Exemple |
|----------|----|--|---------|
| exp  | une liste d'éléments récupérés avec `split_with_sign`  | list  | ["+4x", "+9y"] |
| is_invert  | Faut-il inverser les résultats. Cette variable, par défaut `False`, permet de spécifier si c'est le membre droit ou gauche de l'équation dont on cherche à récupérer les valeurs | bool  | True |

##### Output :

| Ordre | Variable | Description | Type | Exemple |
|----|------|----|--|---------|
| 1 | x | Nombre de `x`  | float  | 1.5 |
| 2 | x | Nombre de `y`  | float  | 7.0 |
| 3 | x | Quotient  | float  | 4.0 |

### Fonction `resoudre_systeme(a, b, c, d, e, f)`

Cette fonction permet de résoudre le système pour les paramètres a, b, c, d, e, f pour le système suivant :

$$
\begin{aligned}
ax + by = e \\
cx + dy = f
\end{aligned}
$$


##### Input :

Variable `a`, `b`, `c`, `d`, `e`, `f`. Variables correspondantes au système ci-dessus

##### Output :

| Ordre | Variable | Description | Type | Exemple |
|----|------|----|--|---------|
| 1 | x | Valeur de `x`  | float  | 1.7 |
| 2 | y | Valeur de `y`  | float  | 7.4 |
