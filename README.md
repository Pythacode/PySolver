# $\textsf{\color{#ba1ce6}{Py}} \textsf {Solver}$

## Présentation du projet

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
> Python doit être installer, sinon, [installer-le]([https://pip.pypa.io/en/stable/installation/](https://www.python.org/downloads/)).
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

#### Fonction `contient_nombre(nbr)`

##### Input :
| Variable | Description | Type | Exemple |
|----------|----|--|---------|
| nbr  | - | str  | "4x" ou "x"  |

##### Output :
bool :
`True` si `nbr` contient un nombre

Cette fonction vérifie si `nbr` contient un nombre. On l'apelleras dans `get_param(exp, is_invert=False)`

### Fonction `split_with_sign(text, sign:str)`

Permet de séparer `text` avec `sign` en gardant le signe, si l'expression n'en à pas déja
