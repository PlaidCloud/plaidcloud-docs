---
title: Dimension Create
description: Créez une nouvelle dimension hiérarchique dans une étape de workflow PlaidCloud pour organiser et structurer votre système de classification des données.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-create.md
---

## Description
Crée une dimension destinée à être utilisée et chargée.


![Dimension Create](/images/dimension_create.png)

## Dimension à créer
### Nom
Vous pouvez utiliser un nom précis pour la dimension à créer, ou inclure des variables pour obtenir un nom dynamique.


Les variables sont utiles lorsque les dimensions sont mises à jour périodiquement et que vous souhaitez conserver une vue historique.

Voici un exemple qui utilise la variable `current_month` pour nommer la dimension de façon dynamique :

```text
dimension_name_{current_month}
```
### Chemin
Les chemins vous permettent de créer des arborescences de dossiers dans lesquelles les dimensions sont stockées. Vous pouvez aussi y utiliser des variables pour rendre l'arborescence dynamique.
Voici un exemple qui utilise la variable `current_month` pour nommer un dossier de façon dynamique :

```text
/Dimensions/{current_month}/Product/
```

### Mémo
Le champ Mémo sert à stocker des commentaires ou des notes.
