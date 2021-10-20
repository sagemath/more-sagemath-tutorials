---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"slideshow": {"slide_type": "slide"}}

# Cours 2: Exploration informatique sur les mots

+++ {"slideshow": {"slide_type": "fragment"}}

Dans cette séance interactive, nous avons exploré comment manipuler des mots avec Python. Nous avons écrit:

- Un petit mémo sur les opérations: [2021-10-19-mots.ipynb](2021-10-19-mots.ipynb)
- Un carnet de labo pour une exploration de propriétés de factorisations: [2021-10-19-carnet-de-labo-factorisations.ipynb](2021-10-19-carnet-de-labo-factorisations.ipynb)

C'était avant tout un **exercice pédagogique** pour entre appercevoir quelques points résumés ci-dessous. Dans la pratique, **Sage contient une importante bibliothèque sur les mots** qui fournit la plupart des utilitaires que nous avons réinventé naïvement. C'est cette bibliothèque que vous allez mettre en action dans le [TP: Combinatoire des mots](combinatoire-des-mots.rst). 

+++ {"slideshow": {"slide_type": "slide"}}

## Résumé de ce que l'on a vu

+++ {"slideshow": {"slide_type": "fragment"}}

### Carnets interactifs (notebooks) Jupyter

#### Utilisation

- Créer un carnet, lui donner un nom.
- Éditer un carnet. Pleins de raccourcis clavier pour être efficace. Apprenez les!!! Voir le menu d'aide de Jupyter.

+++ {"slideshow": {"slide_type": "fragment"}}

#### Cas d'usage

Les carnets permettent de combiner:
- la **narration**: raconter une histoire
- le **calcul** 
- l'**interaction**: dont visualisation, mini-applications, ...

Exemples d'utilisations d'un carnet:
- Calcul interactif
- Documents interactifs:
    - Notes
    - Documents pédagogiques
    - **Carnets de laboratoire**: documenter un calcul, une exploration
    - Blogs, articles, et même diapos!
    - ...

+++ {"slideshow": {"slide_type": "fragment"}}

#### Bonnes pratiques
- Bien séparer:
    - **narration-calcul-interaction**: dans les carnets
    - **programmation**: dans des fichiers
- Des carnets structurés (jeter les autres)
- Des carnets organisés  
  Par exemple par date + thème.

+++ {"slideshow": {"slide_type": "subslide"}}

### Programmation

- Écrire des fonctions pour réutiliser des calculs
- Utiliser des compréhensions pour décrire des ensemble
- Chaque fois que possible écrire ce que l'on fait (calculer **quoi**?) plutôt que comment le faire (calculer **comment**?)
- Un test, c'est précieux: vous avez utilisé du temps cerveau pour le concevoir et le vérifier. Ne jetez pas ce travail à la poubelle!!!
- Le déboggueur pas à pas (pdb)
- **Ne pas réinventer la roue!**

+++ {"slideshow": {"slide_type": "fragment"}}

#### Correspondance prouver $\Longleftrightarrow$ programmer
|     | Prouver | Programmer    |
| --- | --- | --- |
| Le quoi | énoncé d'un théorème | documentation/prototype de la fonction |
| Le quoi | exemples | tests |
| Le comment | démonstration d'un théorème | code |

- C'est une constation pragmatique au quotidien
- C'est aussi un théorème profond (Correspondance de Curry-Howard)

Comme en maths: avant d'attaquer le **comment**, il faut d'abord être clair sur le **quoi**!
- Écrire le prototype et la  documentation
- Écrire des tests
- Ensuite seulement écrire le code

+++ {"slideshow": {"slide_type": "subslide"}}

## Exploration informatique
-   Vos expériences sont précieuses; gardez en une trace  
    Pourquoi: **Reproductibilité**  
    Comment: **Carnets de laboratoire** (comme dans les sciences expérimentales)   
    On en reparlera
