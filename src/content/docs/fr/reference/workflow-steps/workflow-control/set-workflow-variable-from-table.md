---
title: Set Workflow Variable Values from Table
description: Lisez des valeurs dans une table de projet et affectez-les à des variables de workflow, afin que les étapes suivantes se ramifient ou filtrent selon les données plutôt que selon des valeurs codées en dur.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-workflow-variable-from-table.md
---

## Description

Lit des valeurs dans une table de projet et les affecte à des variables de workflow. Utilisez-la pour piloter un workflow à partir de ses propres données — lisez la dernière période clôturée, un nombre de lignes ou un chemin de fichier dans une table de contrôle et laissez les étapes en aval y faire référence.

Les variables définies ici existent pendant la durée de l'exécution du workflow. Pour définir des valeurs qui persistent entre les workflows du projet, utilisez [Set Project Variable Values from Table](/fr/reference/workflow-steps/workflow-control/set-project-variable-from-table/).

## Configuration

### Colonnes source

Associez chaque colonne source à la variable de workflow qu'elle alimente. L'étape lit une seule ligne : réduisez donc la table à une ligne avant son exécution.

### Sélectionner un sous-ensemble de données

Une expression de filtre qui réduit les lignes source — généralement à la seule ligne qui contient les valeurs souhaitées.

### Appliquer un filtre secondaire aux données de résultat

Un filtre de type `HAVING` appliqué après l'agrégation, lorsque la valeur provient d'un calcul groupé.

### Final Data Table Slicing (Limit)

Désactivé par défaut, et limité à une ligne lorsqu'il est activé. Activez-le avec un tri explicite lorsque la source peut renvoyer plusieurs lignes candidates et que vous voulez en obtenir une précise.

## Voir aussi

- [Étapes de contrôle du workflow](/fr/reference/workflow-steps/workflow-control/)
- [Set Workflow Variable](/fr/reference/workflow-steps/workflow-control/set-workflow-variable/)
- [Set Project Variable Values from Table](/fr/reference/workflow-steps/workflow-control/set-project-variable-from-table/)
- [Gérer les variables de workflow](/fr/guides/workflows/manage-workflow-variables/)
