---
title: Set Project Variable Values from Table
description: Lisez des valeurs dans une table de projet et affectez-les à des variables de projet qui persistent d'une exécution de workflow à l'autre.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable-from-table.md
---

## Description

Lit des valeurs dans une table de projet et les affecte à des variables de *projet*. Contrairement à [Set Workflow Variable Values from Table](/fr/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/), les valeurs persistent au-delà de l'exécution — chaque workflow du projet les voit jusqu'à ce que quelque chose les modifie de nouveau.

Utilisez-la pour l'état qui survit à une seule exécution : la dernière période chargée avec succès, un horodatage de repère ou le nom du scénario courant.

## Configuration

### Colonnes source

Associez chaque colonne source à la variable de projet qu'elle alimente. L'étape lit une seule ligne : réduisez donc la table à une ligne avant son exécution.

### Sélectionner un sous-ensemble de données

Une expression de filtre qui réduit les lignes source.

### Appliquer un filtre secondaire aux données de résultat

Un filtre de type `HAVING` appliqué après l'agrégation.

### Final Data Table Slicing (Limit)

Désactivé par défaut, et limité à une ligne lorsqu'il est activé. Activez-le avec un tri explicite lorsque la source peut renvoyer plusieurs lignes candidates.

## Voir aussi

- [Étapes de contrôle du workflow](/fr/reference/workflow-steps/workflow-control/)
- [Set Project Variable](/fr/reference/workflow-steps/workflow-control/set-project-variable/)
- [Set Workflow Variable Values from Table](/fr/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/)
