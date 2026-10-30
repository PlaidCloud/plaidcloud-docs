---
title: Table Restore to Timestamp
description: Restaurez sur place une table PlaidCloud à son instantané le plus récent pris à un instant donné ou avant, sous forme d'étape de workflow.
sidebar:
  order: 45
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-restore-timestamp.md
---

## Description

**Table : restaurer à un horodatage** remplace sur place une table par son instantané le plus récent pris à un instant donné ou avant. Utilisez-la pour ramener une table à son état à la fin d'une période, ou avant un chargement qui s'est mal passé. La restauration modifie la table elle-même : toutes les étapes et tous les tableaux de bord qui la lisent voient donc les lignes restaurées.

## Restaurer à un instant donné

| Paramètre | Obligatoire | Fonction |
| --- | --- | --- |
| Table | Oui | La table à restaurer. |
| Horodatage | Oui | L'instant, sous forme d'heure ISO-8601 comme `2026-09-30T23:59:59Z` ou de secondes écoulées depuis 1970. Une heure sans fuseau est en UTC. Une variable de workflow comme `{restore_time}` convient aussi. |
| Un instantané pris exactement à l'horodatage est pris en compte | Non | Activé par défaut. Désactivez-le pour restaurer uniquement un instantané pris avant l'horodatage. |

Lorsqu'aucun instantané n'a été pris à l'horodatage ou avant, l'étape se termine avec un avertissement, laisse la table telle quelle et le workflow se poursuit. Une table introuvable se termine aussi avec un avertissement. Sur un moteur de stockage qui ne conserve que des instantanés nommés, la table ne peut être restaurée qu'à un instantané pris exactement à l'horodatage ; prenez un instantané nommé à l'instant auquel vous voudrez revenir.

## Voir aussi

- [Restaurer les tables](/fr/reference/workflow-steps/import/restore-tables/)
- [Étapes de table](/fr/reference/workflow-steps/tables/)
