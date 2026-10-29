---
title: Dimension Delete
description: "Supprimez une dimension de PlaidCloud dans une étape de workflow pour retirer les structures de données hiérarchiques devenues inutiles."
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-delete.md
---

## Description
Supprime une dimension ainsi que toute la structure, les valeurs, les propriétés, les alias et les hiérarchies alternatives associés


![Dimension Clear](/images/dimension_clear.png)



## Sélection de la dimension
### Spécifier la dimension dynamiquement
Si des **dimensions** ou des **chemins** ont été créés dynamiquement, les mêmes variables peuvent servir à les supprimer. Utiliser des variables dans le processus de suppression est pratique, car cela évite de devoir mettre à jour manuellement l'étape Dimension Delete à intervalles réguliers.



Exemple qui utilise la variable `current_month` pour supprimer dynamiquement la dimension Materials :

```text
/Dimensions/{current_month}/Products/Materials
```

### Utiliser une dimension spécifique

Utilisez la liste déroulante pour sélectionner la dimension spécifique à supprimer.
