---
title: Dimension Sort
description: "Triez automatiquement les membres d'une dimension dans une étape de workflow PlaidCloud afin de conserver un ordre cohérent au sein de vos hiérarchies."
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-sort.md
---

## Description

Trie les membres d'une dimension sous leurs parents : par ordre alphabétique, par valeur, par propriété ou selon une colonne d'ordre personnalisée. Évite la fastidieuse tâche de faire glisser manuellement les membres de la hiérarchie dans le bon ordre, ce qui est particulièrement utile après un chargement en masse ou une restructuration importante.

Agit directement sur la dimension ; aucune table source ni cible n'est nécessaire.


## Sélection de la dimension
### Spécifier la dimension dynamiquement
Si des **dimensions** ou des **chemins** ont été créés dynamiquement, les mêmes variables peuvent servir à les trier. Utiliser des variables dans le processus de tri est pratique, car cela évite de devoir mettre à jour manuellement l'étape Dimension Sort à intervalles réguliers.



Exemple qui utilise la variable `current_month` pour trier dynamiquement la dimension Materials :

```text
/Dimensions/{current_month}/Products/Materials
```

### Utiliser une dimension spécifique

Utilisez la liste déroulante pour sélectionner la dimension spécifique à trier.
