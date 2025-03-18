# $\textsf{\color{#ba1ce6}{Py}} \textsf {Solver}$

## Somaire

- Présentation du projet
- Instalation
- Utilisation
- Explication du code

## Présentation du projet

> [!WARNING]
> Ce projet n'est en aucun cas certifié infaillible, il peut donc contenir des bugs... Merci de votre compréhension.
> Si vous en trouvez un, vous pouvez me le faire parvenir en [créant une issue](https://github.com/Pythacode/PySolver/issues), **avec la sortie console**

Ce projet à été cré dans le cadre de cours de math.
Il s'agit d'un code en ligne de commande permetant de résoudre un système d'équation à deux inconu (`x` & `y`) et à deux ligne. Attention, ce programme ne peut pas faire de produit.

## Installation

Pour installer le projet, téléchargez le avec 
```cmd
git clone https://github.com/Pythacode/PySolver.git
```
ou avec le ficher zip.

Ensuite, rentrer dans le dossier du projet, puis intaller les dépandance avec
```cmd
pip install -r requirements.txt
```

> [!TIP]
> Python doit être installer, sinon, [installer-le](https://www.python.org/downloads/).
> Pip doit également être instalé, sinon, [installer-le](https://pip.pypa.io/en/stable/installation/) ou ajoutez `python -m` au début de la commande.

## Utilisation 

Pour utiliser le programe, il faut le lancer dans un terminal avec
```cmd
python main.py
```
ou
```cmd
python3 main.py
```

Le programe vous demanderas d'entrer les deux expression l'une après l'autre.

> [!IMPORTANT]
> Veillez à utiliser uniquement `x` et `y` pour les inconus, et `+`, `-`, `=` pour les signes. Ce programmes ne peut pas faire de produit.

## Explication du code

Pour tous ceux & celle qui veulent améliorer le code, le modifier, ajouter une UI, cette section est faite pour toi :

### Fichier `main.py`

> [!TIPS]
> Souvent, le code est commenté ligne par ligne dans le fichier. Si tu ne comprend pas cet explication, lis le code, tu comprendras peut-être mieux

#### Fonction `contient_nombre(nbr)`

Cette fonction vérifie si `nbr` contient un nombre. On l'apelleras dans `get_param(exp, is_invert=False)`

##### Input :
| Variable | Description | Type | Exemple |
|----------|----|--|---------|
| nbr  | Variable à verifier si il y à nombre | str  | "4x" ou "x"  |

##### Output :
bool :
`True` si `nbr` contient un nombre

### Fonction `split_with_sign(text, sign:str)`

Permet de séparer `text` avec `sign` en gardant le signe, si l'expression n'en à pas déja (`+` ou `-`)

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
| exp  | une liste d'élément récuperer avec `split_with_sign`  | list  | ["+4x", "+9y"] |
| is_invert  | Faut-il inverser les résultat. Cette variable, par default `False`, permer de spécifier si c'est le membre droit ou gauche de l'équation dont on cherche à récuperer les valeurs | bool  | True |

##### Output :

| Ordre | Variable | Description | Type | Exemple |
|----|------|----|--|---------|
| 1 | x | Nombre de `x`  | float  | 1.5 |
| 2 | x | Nombre de `y`  | float  | 7.0 |
| 3 | x | Quotient  | float  | 4.0 |

### Fonction `resoudre_systeme(a, b, c, d, e, f)`

Cette fonction permet de résoudre le système pour les paramètres a, b, c, d, e, f pour le système suivant :

$$
\documentclass{article}
\begin{document}
\[
\left \{
\begin{array}{c @{=} c}
    x & \sin a \cos b \\
    y & \sin a \sin b
\end{array}
\right.
\]
\end{document}
$$

##### Input :

Variable `a`, `b`, `c`, `d`, `e`, `f`. Variable correspondante au système ci-dessus

##### Output :

| Ordre | Variable | Description | Type | Exemple |
|----|------|----|--|---------|
| 1 | y | Valeur de `x`  | float  | 1.7 |
| 2 | x | Valeur de `y`  | float  | 7.4 |

