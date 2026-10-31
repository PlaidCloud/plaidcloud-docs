---
title: Solveur
description: Résolvez des problèmes d'optimisation LP et MIP à partir des données de tables d'un workflow.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/optimization/solver.md
---

L'étape Solveur résout des problèmes de programmation linéaire et de programmation en nombres entiers mixtes à partir de tables PlaidCloud. Utilisez-la lorsqu'un workflow doit choisir des valeurs qui minimisent ou maximisent un objectif tout en respectant des contraintes linéaires.

Le Solveur s'exécute dans un pod de job de workflow et réécrit les résultats dans des tables de projet.

## Entrées

Configurez quatre tables d'entrée. Chaque entrée comporte une table source, un mappage de données et des filtres. PlaidCloud traduit ces paramètres en requête de base de données utilisée pour lire chaque entrée : la sélection a donc lieu avant que le Solveur ne reçoive les lignes.

### Variables

Une ligne par variable de décision.

| Colonne | Description |
| --- | --- |
| `variable_id` | Nom unique de la variable, utilisé par les autres tables d'entrée. |
| `lower_bound` | Valeur minimale. Laissez vide pour ne définir aucune borne inférieure. |
| `upper_bound` | Valeur maximale. Laissez vide pour ne définir aucune borne supérieure. |
| `type` | `continuous`, `integer` ou `binary`. Les variables binaires utilisent les bornes `0` et `1`. |

### Objectif

Une ligne par variable ayant un coefficient d'objectif non nul.

| Colonne | Description |
| --- | --- |
| `variable_id` | Variable issue de l'entrée Variables. |
| `coefficient` | Coefficient d'objectif de cette variable. |

Les variables absentes de cette table utilisent le coefficient `0`.

### Contraintes

Une ligne par contrainte linéaire.

| Colonne | Description |
| --- | --- |
| `constraint_id` | Nom unique de la contrainte, utilisé par l'entrée Coefficients. |
| `lower_bound` | Activité minimale autorisée. Laissez vide pour ne définir aucune borne inférieure. |
| `upper_bound` | Activité maximale autorisée. Laissez vide pour ne définir aucune borne supérieure. |

Définissez la même borne inférieure et la même borne supérieure pour une contrainte d'égalité.

### Coefficients

Matrice creuse des coefficients de contraintes.

| Colonne | Description |
| --- | --- |
| `constraint_id` | Contrainte issue de l'entrée Contraintes. |
| `variable_id` | Variable issue de l'entrée Variables. |
| `coefficient` | Coefficient de cette variable dans cette contrainte. |

## Options du solveur

| Option | Description |
| --- | --- |
| Sens de l'objectif | Choisissez Minimiser ou Maximiser. |
| Limite de temps | Limite de durée d'exécution facultative, en secondes. |
| Écart MIP | Écart MIP relatif facultatif pour les problèmes en nombres entiers mixtes. |
| Activer le présolve | Laisse le solveur simplifier le modèle avant la résolution. |
| Utiliser des ressources personnalisées | Définit les cœurs de processeur et la mémoire du pod de job. |

## Sorties

Le Solveur écrit trois tables de sortie.

### Table de solution

Contient une ligne par variable avec la valeur résolue, les bornes, le type de variable, le coefficient d'objectif et, lorsqu'il est disponible, le coût réduit.

### Table des résultats de contraintes

Contient une ligne par contrainte avec l'activité, les bornes, la marge et, lorsqu'elle est disponible, la valeur duale.

### Table récapitulative

Contient une ligne avec le statut du solveur, la valeur de l'objectif, la durée d'exécution, l'écart MIP, la borne duale MIP, le nombre de nœuds, le nombre d'itérations, le nombre de variables et le nombre de contraintes.

## Comportement selon le statut

Une résolution optimale termine l'étape avec succès. Si le solveur renvoie une solution exploitable avec un statut non optimal, l'étape se termine avec un avertissement et écrit tout de même les tables de sortie. Si aucune solution exploitable n'est disponible, l'étape échoue avec le message de statut du solveur.
