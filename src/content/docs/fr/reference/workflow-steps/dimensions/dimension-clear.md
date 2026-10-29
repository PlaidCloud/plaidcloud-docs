---
title: Dimension Clear
description: "Supprimez tous les membres d'une dimension PlaidCloud dans une étape de workflow, tout en conservant la structure et la configuration de la dimension."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-clear.md
---

## Description
Efface le contenu d'une dimension, y compris la structure, les valeurs, les alias, les propriétés et les hiérarchies alternatives


![Dimension Clear](/images/dimension_clear.png)



## Sélection de la dimension
### Spécifier la dimension dynamiquement
Si des **dimensions** ou des **chemins** ont été créés dynamiquement, les mêmes variables peuvent servir à les effacer. Utiliser des variables dans le processus d'effacement est pratique, car cela évite de devoir mettre à jour manuellement l'étape Dimension Clear à intervalles réguliers.



Exemple qui utilise la variable `current_month` pour effacer dynamiquement la dimension Materials :

```text
/Dimensions/{current_month}/Products/Materials
```

### Utiliser une dimension spécifique

Utilisez la liste déroulante pour sélectionner la dimension spécifique à effacer.
