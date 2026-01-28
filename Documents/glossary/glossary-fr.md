<h1>
    <a href="README-FR.md"><img src="https://img.icons8.com/color/48/000000/france-circular.png" width="30" alt="Français"/></a>
    <a href="README.md"><img src="https://img.icons8.com/color/48/000000/great-britain-circular.png" width="30" alt="English"/></a> 
    Glossaire — NGL
</h1>

### NGL (Node Graph Language)
Langage déclaratif typé destiné à décrire des graphes sous forme textuelle et compilable.

### Fichier Source NGL
Fichier texte avec l’extension `.ngl`, contenant une  définitions d'un graphe.

### Node
Entité fondamentale d’un graph.
Un node possède :
- un identifiant unique
- un type explicite
- un ensemble optionnel d’attributs

Un node représente une étape, une action ou une décision dans un flowchart.

### Edge
Lien directionnel entre deux nodes.
Un edge exprime un flux logique dans le graph.

Un edge peut posséder :
- une source
- une cible
- des attributs optionnels (label, condition, etc.)

### Compiler
Ensemble des étapes transformant un fichier .ngl en une sortie graphique.
Le compilateur NGL suit un pipeline strict :
- parsing
- validation
- normalisation
- rendering
- export

### Parser
Composant chargé de transformer le texte source en une structure syntaxique (AST).
Le parser ne valide pas la logique métier.

### AST
Représentation structurée et indépendante du rendu du graph source.
L’AST est immuable et constitue la frontière centrale du compilateur.

### Validator
Composant chargé de vérifier la cohérence du graph :
- références valides
- types compatibles
- règles propres au graph type

Aucune correction automatique n’est effectuée.

### Normalizer
Étape transformant l’AST validé en une forme normalisée, explicite et exploitable par le renderer.
Exemples :
- résolution des valeurs par défaut
- expansion des syntaxes implicites

### Renderer
Composant chargé de transformer l’AST normalisé en primitives graphiques.
Le renderer ne contient aucune logique métier.

### Exporter
Composant responsable de la génération du format final (SVG, PNG, etc.).

### Diagnostic
Message structuré produit par le compilateur pour signaler :
- erreurs
- avertissements
- informations

Les diagnostics sont précis, localisés et explicites.

### Strict Mode
Mode par défaut de NGL où toute ambiguïté ou incohérence entraîne une erreur de compilation.