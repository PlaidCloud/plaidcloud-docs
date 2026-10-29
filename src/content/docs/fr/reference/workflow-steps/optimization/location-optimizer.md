---
title: Optimiseur de localisation
description: Choisissez K sites parmi un ensemble de candidats qui minimisent la distance totale ou pondérée jusqu'à un ensemble de points de demande.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/optimization/location-optimizer.md
---

L'étape Optimiseur de localisation choisit **K** sites dans une table d'emplacements candidats qui minimisent la distance totale ou pondérée jusqu'à une table de points de demande : un modèle de localisation d'installations de type p-médian, résolu comme un programme en nombres entiers mixtes sur le solveur HiGHS de PlaidCloud.

L'Optimiseur de localisation s'exécute dans un pod de job de workflow, la même image de job que celle utilisée par [Solveur](/fr/reference/workflow-steps/optimization/solver/), et réécrit les résultats dans des tables de projet.

## Entrées

### Sites candidats

La table des emplacements de sites possibles, mappée avec le même mappage de colonnes source/cible, les mêmes filtres et la même agrégation que toute entrée mappée sur une table.

### Points de demande

La table des points dont la distance au site sélectionné le plus proche est minimisée, mappée de la même manière.

### Table de distances (facultative)

Une table précalculée des distances entre candidats et points de demande. Laissez-la non définie pour que l'étape calcule elle-même les distances.

### K

Le nombre de sites à sélectionner parmi les sites candidats.

## Options du solveur

| Option | Description |
| --- | --- |
| Limite de temps | Limite de durée d'exécution facultative, en secondes. |
| Écart MIP | Écart MIP relatif facultatif. |
| Activer le présolve | Laisse le solveur simplifier le modèle avant la résolution. Activé par défaut. |
| Utiliser des ressources personnalisées | Définit les cœurs de processeur et la mémoire du pod de job. |

Un arrêt dû à la **Limite de temps** ou à l'**Écart MIP** renvoie la meilleure solution trouvée dans cette limite plutôt que l'optimum réel, le même compromis que fait [Solveur](/fr/reference/workflow-steps/optimization/solver/#comportement-selon-le-statut) avec un statut non optimal. Laissez les deux non définis pour résoudre jusqu'à l'optimalité complète.

## Sorties

L'Optimiseur de localisation écrit trois tables de sortie, qui doivent toutes porter des noms distincts.

### Table de sortie des sites sélectionnés

Une ligne par site choisi.

### Table de sortie des affectations

Une ligne par point de demande, indiquant le site sélectionné auquel il a été affecté.

### Table de sortie récapitulative

Une ligne avec le statut du solveur, la valeur de l'objectif et les détails de l'exécution.

## Limites et réserves

Cette étape est un modèle **p-médian** : elle minimise toujours la distance totale (éventuellement pondérée) entre les points de demande et leur site sélectionné le plus proche. Elle ne permet pas d'exprimer un score de type gravitaire, une formule de scoring personnalisée, ni aucun objectif où un score plus élevé est préférable à une distance plus faible. Un problème de sélection de sites qui requiert l'un de ces éléments relève plutôt d'un modèle [Solveur](/fr/reference/workflow-steps/optimization/solver/) construit à la main.

## Voir aussi

- [Solveur](/fr/reference/workflow-steps/optimization/solver/) : optimisation linéaire et en nombres entiers mixtes générale, pour un objectif de sélection de sites que le modèle p-médian fixe de cette étape ne couvre pas.
- [Matrice de conversion Alteryx](/fr/reference/alteryx-conversion-matrix/) : l'outil Alteryx Location Optimizer ne se convertit vers cette étape que pour son cas de minimisation linéaire de la distance ; un noyau gravitaire ou une macro de scoring personnalisée reste refusé.
