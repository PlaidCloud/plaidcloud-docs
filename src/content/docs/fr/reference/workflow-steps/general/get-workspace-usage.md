---
title: Étape Get Workspace Usage
description: Écrit dans une table de projet les totaux d'utilisation de l'espace de travail issus de Rapports d'utilisation, par jour ou par mois, pour représenter l'adoption sous forme de graphique ou alimenter une étape en aval.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Description

Écrit dans une table de projet un résumé de l'utilisation de votre espace de travail. Servez-vous-en pour suivre l'adoption dans le temps, pour créer vos propres tableaux de bord d'utilisation ou pour signaler une baisse d'activité dans un workflow planifié. Les chiffres sont les mêmes que ceux affichés par [Rapports d'utilisation](/fr/administration/access/usage-reports/).

La sortie ne contient que des totaux. Aucune ligne ne nomme un membre, et les chemins de notebooks sont remplacés par `*`. Les membres dont l'utilisation a été effacée sont exclus.

## Configuration

### Données d'utilisation

**Jeu de données** choisit ce que contient chaque ligne :

| Jeu de données | Une ligne pour chaque | Colonnes |
|---|---|---|
| **Quotidien par élément** | Jour, domaine, événement et sujet | `day`, `source`, `event`, `subject`, `events` |
| **Mensuel par élément** | Mois, domaine, événement et sujet | `month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial` |
| **Totaux mensuels** (par défaut) | Mois et domaine | `month`, `source`, `active_users`, `coverage_start`, `partial` |

`partial` est vrai pour un mois que l'historique ne couvre pas entièrement, et `coverage_start` est la date à laquelle la collecte a commencé.

**Domaine** limite les lignes à un domaine : **Application PlaidCloud**, **Tableaux de bord**, **Applications**, **Visites d'applications** ou **Notebooks**. Laissez **Tous les domaines** pour les inclure tous.

### Plage de dates

**Plage** choisit les jours à lire :

- **Nombre de derniers jours** (30 par défaut) lit les jours les plus récents, aujourd'hui compris.
- **Mois précédent** lit le dernier mois calendaire complet.
- **Cumul du mois** lit du premier jour de ce mois à aujourd'hui.
- **Entre deux dates** lit de **Date de début** à **Date de fin**. Laissez **Date de fin** vide pour lire jusqu'à aujourd'hui.

Les jours et les dates sont en UTC. **Jours**, **Date de début** et **Date de fin** acceptent une [variable](/fr/guides/workflows/manage-workflow-variables/) telle que `{report_start}`, ainsi qu'un nombre ou une date au format `YYYY-MM-DD`. Le début ne doit pas être postérieur à la fin.

### Cible de l'utilisation

**Table cible** reçoit le résultat. L'étape remplace le contenu de la table et écrit toujours les colonnes du jeu de données, même lorsqu'il n'y a aucune ligne.

## Avertissements

Ils ne font pas échouer l'étape. Elle se termine avec un avertissement qui indique ce qui s'est passé, et écrit tout de même la table :

- La collecte de l'utilisation n'est pas encore configurée pour l'espace de travail.
- Il n'y a eu aucune utilisation dans la plage.
- La plage commence avant ce qui est conservé ; elle a donc été raccourcie pour commencer là où l'historique débute. Les données quotidiennes sont conservées 180 jours et les données mensuelles 25 mois.

## Journal de sécurité

Chaque exécution écrit une entrée dans le Journal de sécurité qui consigne le jeu de données, la plage, la table cible, le workflow, l'étape et l'exécution, ainsi que le nombre de lignes écrites.

## Voir aussi

- [Étapes générales](/fr/reference/workflow-steps/general/)
- [Rapports d'utilisation](/fr/administration/access/usage-reports/)
- [Get Workspace Members](/fr/reference/workflow-steps/general/get-workspace-members/) (étape)
