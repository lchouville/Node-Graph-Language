<h1>
    <a href="README-FR.md"><img src="https://img.icons8.com/color/48/000000/france-circular.png" width="30" alt="Français"/></a>
    <a href="README.md"><img src="https://img.icons8.com/color/48/000000/great-britain-circular.png" width="30" alt="English"/></a> 
    Node Graph Language
</h1>

## ℹ️ Introduction
**Node Graph Language *(NGL)*** est un langage déclaratif typé et un compilateur permettant de décrire et de générer des structures basées sur des graphes à partir de fichiers texte brut.

**NGL** met l'accent sur le typage explicite, la validation stricte et un pipeline de compilation propre, transformant les fichiers `.ngl` en sorties visuelles telles que `SVG` ou `PNG`.

Le projet est intentionnellement conçu comme un compilateur, et non comme un outil de rendu. Les fichiers source sont analysés dans un arbre syntaxique abstrait `(AST)`, validés, normalisés, puis rendus via un backend dédié.

### Portée actuelle

La mise en œuvre initiale de **NGL** cible uniquement les organigrammes.
- Cette limitation est délibérée : elle permet aux règles du langage, au système de types et au pipeline de compilation de rester stricts et prévisibles, tout en gardant l'architecture ouverte à de futurs types de graphes tels que :
- les machines à états
- les graphes de dépendance
- les pipelines d'exécution
- les systèmes basés sur des nœuds

### Objectif de conception

**NGL** est construit autour des principes suivants :
- Syntaxe stricte : aucun comportement ambigu ou implicite
- Nœuds et arêtes typés : les erreurs de structure sont détectées tôt
- Séparation des préoccupations : l'analyse, la validation et le rendu sont isolés
- Extensibilité : de nouveaux types de graphes peuvent être ajoutés sans perturber ceux qui existent déjà
- Approche axée sur les outils : le langage est conçu pour prendre en charge les outils d'édition (par exemple, les extensions VS Code)

### Format de fichier

Les fichiers source **NGL** utilisent l'extension `.ngl`.

### État d'avancement du projet

**NGL** en est actuellement à un stade précoce de développement.
L'accent est mis sur la définition du langage, l'architecture du compilateur et la prise en charge des organigrammes avant de passer à d'autres types de graphiques.

## 🛠️ Installation

## 📚 Documentations

## 👤 Auteurs & Collaborateurs

<table style="border-collapse: collapse; border: none; width: 100%">