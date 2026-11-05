---
title: Get Workspace Usage (étape)
description: Écrit dans une table de projet les totaux d'utilisation de l'espace de travail issus des rapports d'utilisation, par jour ou par mois, pour suivre l'adoption dans un graphique ou alimenter une étape en aval.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Description

Écrit dans une table de projet un récapitulatif de l'utilisation de votre espace de travail. Utilisez-la pour suivre l'adoption dans le temps, créer vos propres tableaux de bord d'utilisation ou signaler une baisse d'activité dans un workflow planifié. Les chiffres sont les mêmes que ceux que présentent les [Rapports d'utilisation](/fr/administration/access/usage-reports/).

La sortie ne contient que des totaux. Aucune ligne ne nomme un membre, et les chemins de notebook sont remplacés par `*`. Les membres dont l'utilisation a été effacée sont exclus.

## Configuration

### Données d'utilisation

**Jeu de données** détermine le contenu de chaque ligne :

| Jeu de données | Une ligne pour chaque | Colonnes |
|---|---|---|
| **Daily per item** | Jour, domaine, événement et sujet | `day`, `source`, `event`, `subject`, `events` |
| **Monthly per item** | Mois, domaine, événement et sujet | `month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial` |
| **Monthly totals** (par défaut) | Mois et domaine | `month`, `source`, `active_users`, `coverage_start`, `partial` |

`partial` vaut true pour un mois que l'historique ne couvre pas en totalité, et `coverage_start` est la date à laquelle la collecte a commencé.

**Area** limite les lignes à un seul domaine : **Application PlaidCloud**, **Tableaux de bord**, **Applications**, **Visites d'applications** ou **Notebooks**. Laissez la valeur **All areas** pour les inclure tous.

### Plage de dates

**Range** détermine les jours à lire :

- **Last number of days** (30 par défaut) lit les jours les plus récents, aujourd'hui compris.
- **Previous month** lit le dernier mois civil complet.
- **Cumul du mois** lit du premier jour du mois en cours jusqu'à aujourd'hui.
- **Between dates** lit de la **Date de début** à la **Date de fin**. Laissez **Date de fin** vide pour lire jusqu'à aujourd'hui.

Les jours et les dates sont en UTC. **Jours**, **Date de début** et **Date de fin** acceptent une [variable](/fr/guides/workflows/manage-workflow-variables/) telle que `{report_start}`, ainsi qu'un nombre ou une date au format `YYYY-MM-DD`. La date de début ne doit pas être postérieure à la date de fin.

### Cible d'utilisation

**Table cible** reçoit le résultat. L'étape remplace tout le contenu de la table et écrit toujours les colonnes du jeu de données, même s'il n'y a aucune ligne.

## Avertissements

Ces cas ne font pas échouer l'étape. Elle se termine avec un avertissement qui indique ce qui s'est produit et écrit tout de même la table :

- La collecte de l'utilisation n'est pas encore configurée pour l'espace de travail.
- Il n'y avait aucune utilisation dans la plage.
- La plage commence avant les données conservées ; elle a donc été tronquée pour commencer là où l'historique débute. Les données quotidiennes sont conservées 180 jours et les données mensuelles 25 mois.

## Journal de sécurité

Chaque exécution écrit une entrée dans le journal de sécurité qui consigne le jeu de données, la plage, la table cible, le workflow, l'étape et l'exécution, ainsi que le nombre de lignes écrites.

## Voir aussi

- [Étapes générales](/fr/reference/workflow-steps/general/)
- [Rapports d'utilisation](/fr/administration/access/usage-reports/)
- [Get Workspace Members (étape)](/fr/reference/workflow-steps/general/get-workspace-members/)
