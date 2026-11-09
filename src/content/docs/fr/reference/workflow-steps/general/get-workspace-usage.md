---
title: Get Workspace Usage
description: Écrivez dans une table de projet les totaux d'utilisation de l'espace de travail issus des Rapports d'utilisation, par jour ou par mois, pour suivre l'adoption ou alimenter une étape en aval.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Description

Écrit l'utilisation de votre espace de travail dans une table de projet. Utilisez-la pour suivre l'adoption dans le temps, pour produire des rapports d'utilisation par service ou par équipe, pour créer vos propres tableaux de bord, ou pour signaler une baisse d'activité dans un workflow planifié. Les chiffres sont les mêmes que ceux affichés par les [Rapports d'utilisation](/fr/administration/access/usage-reports/).

Trois jeux de données ne contiennent que des totaux : aucune ligne ne nomme un membre, et les chemins de notebooks sont remplacés par `*`. Les quatre autres (**Membres**, **Quotidien par membre**, **Contenu** et **Contenu par membre**) sont conçus pour le reporting. **Membres**, **Quotidien par membre** et **Contenu par membre** contiennent l'identité des membres (ID utilisateur, nom d'utilisateur, e-mail, prénom, nom et groupes de sécurité) : traitez donc la table cible comme vous traiteriez n'importe quelle liste de membres. Chaque exécution de l'étape est consignée dans le Journal de sécurité.

## Configuration

### Données d'utilisation

**Jeu de données** détermine ce que contient chaque ligne :

| Jeu de données | Valeur | Une ligne pour chaque | Contient l'identité |
|---|---|---|---|
| **Quotidien par élément** | `daily_item` | Jour, domaine, événement et sujet | Non |
| **Mensuel par élément** | `monthly_item` | Mois, domaine, événement et sujet | Non |
| **Totaux mensuels** (par défaut) | `monthly_tenant` | Mois et domaine | Non |
| **Membres** | `members` | Personne dans l'espace de travail | Oui |
| **Quotidien par membre** | `daily_user` | Personne, jour et domaine | Oui |
| **Contenu** | `content` | Tableau de bord, application ou notebook | Non |
| **Contenu par membre** | `content_user` | Personne et élément | Oui |

**Domaine** limite les lignes à un seul domaine. Laissez **Tous les domaines** pour les inclure tous.

| Domaine | Valeur |
|---|---|
| **Tous les domaines** (par défaut) | `""` |
| **Application PlaidCloud** | `plaidclient` |
| **Tableaux de bord** | `superset` |
| **Applications** | `panel` |
| **Visites d'apps** | `panel_visit` |
| **Serveurs de notebooks** | `jupyterhub` |
| **Notebooks** | `jupyter` |

Ces valeurs sont celles que contient une étape lorsque vous la créez ou la modifiez via l'API ou un assistant IA.

### Colonnes

#### Quotidien par élément

`day`, `source`, `event`, `subject`, `events`.

#### Mensuel par élément

`month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial`.

#### Totaux mensuels

`month`, `source`, `active_users`, `coverage_start`, `partial`.

`partial` vaut true pour un mois que l'historique ne couvre pas entièrement, et `coverage_start` est la date à laquelle la collecte a commencé. Un mois est inclus 3 jours après sa clôture, une fois ses chiffres stabilisés.

#### Colonnes des membres

**Membres**, **Quotidien par membre** et **Contenu par membre** commencent par les mêmes sept colonnes :

| Colonne | Contient |
|---|---|
| `user_id` | L'ID du membre. |
| `user_name` | Le nom d'utilisateur du membre. |
| `email` | L'adresse e-mail du membre, en minuscules. |
| `first_name` | Le prénom. |
| `last_name` | Le nom. |
| `is_active` | True lorsque le membre est actif, false lorsqu'il est désactivé. |
| `groups` | Les groupes de sécurité du membre, séparés par `; `. |

`groups` ne liste que les groupes de premier niveau. Les sous-groupes ne sont pas développés.

#### Membres

Les colonnes des membres, puis :

| Colonne | Contient |
|---|---|
| `first_seen` | Le premier jour où le membre a utilisé PlaidCloud, quelle que soit la plage de dates. Lorsque vous définissez un **Domaine**, il s'agit du premier jour dans ce domaine. |
| `last_seen` | Le dernier jour d'activité du membre dans la plage. |
| `active_days` | Les jours avec activité dans la plage. |
| `events` | Les événements d'activité dans la plage. |
| `active_minutes` | Les minutes d'activité. Les minutes qui se chevauchent entre domaines ne sont comptées qu'une fois. |
| `session_minutes` | Les minutes en session. |
| `app_open_minutes` | Les minutes pendant lesquelles le membre a gardé des applications Panel ouvertes. |

Chaque membre a une ligne, sauf les membres dont l'utilisation a été effacée. Les comptes de service et les agents ne sont pas listés. Un membre sans activité dans la plage a des valeurs vides après `groups`. Les totaux correspondent à ceux des [Rapports d'utilisation](/fr/administration/access/usage-reports/), sauf pour les membres supprimés depuis.

#### Quotidien par membre

Les colonnes des membres, puis `day`, `source` (le domaine), `events`, `active_minutes`, `session_minutes`, `first_at` et `last_at` (les heures de première et de dernière activité ce jour-là).

#### Contenu

| Colonne | Contient |
|---|---|
| `type` | `dashboard`, `panel_app`, `wasm_app` ou `notebook`. |
| `subject` | L'ID de l'élément. Tous les notebooks partagent une seule ligne, avec `*` ici. |
| `name` | Le nom de l'élément, ou `*` pour les notebooks. |
| `deleted` | True lorsque l'élément a été supprimé depuis. |
| `users` | Les membres qui l'ont ouvert. |
| `opens` | Le nombre d'ouvertures. |
| `last_used` | La date de dernière utilisation. |
| `app_open_minutes` | Les minutes pendant lesquelles des applications Panel étaient ouvertes. |

#### Contenu par membre

Les colonnes des membres, puis `type`, `subject`, `name` (comme dans **Contenu**), `opens` (le nombre de fois où ce membre a ouvert l'élément) et `last_day` (le dernier jour d'utilisation du membre).

### Remarques sur les jeux de données des membres

- L'activité des agents, des comptes de service et des membres supprimés depuis a des colonnes d'identité vides. Un membre supprimé ne conserve que son `user_id`.
- Les ouvertures dans **Contenu** peuvent dépasser la somme des ouvertures dans **Contenu par membre**. La différence correspond aux ouvertures qui ne peuvent pas être attribuées à un membre, comme les vues intégrées ou invitées d'un tableau de bord. **Contenu** les compte, ce que **Contenu par membre** ne peut pas faire.

### Exemple : minutes actives par service

**Membres** et **Contenu par membre** contiennent l'`email` du membre, en minuscules, ce qui vous permet de les joindre à une table de votre choix, comme une table RH ou une table de référence de l'organisation, et de produire un rapport par service.

1. Ajoutez une étape **Get Workspace Usage** avec **Jeu de données** défini sur **Membres**, et une table cible telle que `usage_members`.
2. Ajoutez une étape **Table : jointure interne** qui joint `usage_members` à votre table d'organisation là où les colonnes `email` en minuscules correspondent. Conservez le service issu de votre table, ainsi que les colonnes `active_minutes` et `events` de `usage_members`.
3. Dans la même étape, agrégez par service et faites la somme de `active_minutes`.

Le résultat donne les minutes actives par service. Les membres absents de votre table d'organisation disparaissent d'une jointure interne ; utilisez donc une jointure gauche si vous souhaitez les voir. Répétez l'opération avec une seconde étape sur **Contenu par membre** et faites la somme de `opens` par service pour savoir qui utilise quels tableaux de bord et quelles applications.

### Plage de dates

**Plage** détermine les jours à lire :

| Plage | Valeur | Lit |
|---|---|---|
| **Nombre de derniers jours** (30 par défaut) | `last_days` | Les jours les plus récents, aujourd'hui inclus. |
| **Mois précédent** | `previous_month` | Le dernier mois calendaire complet. |
| **Cumul du mois** | `month_to_date` | Du premier jour du mois en cours jusqu'à aujourd'hui. |
| **Entre deux dates** | `dates` | De **Date de début** à **Date de fin**. Laissez **Date de fin** vide pour lire jusqu'à aujourd'hui. |

Les jours et les dates sont en UTC. **Jours**, **Date de début** et **Date de fin** acceptent une [variable](/fr/guides/workflows/manage-workflow-variables/) telle que `{report_start}`, ainsi qu'un nombre ou une date au format `YYYY-MM-DD`. Le début ne doit pas être postérieur à la fin.

### Cible de l'utilisation

**Table cible** reçoit le résultat. L'étape remplace tout ce que la table contenait, et écrit toujours les colonnes du jeu de données, même lorsqu'il n'y a aucune ligne.

## Avertissements

Ces cas ne font pas échouer l'étape. Elle se termine avec un avertissement qui indique ce qui s'est passé, et écrit quand même la table :

- La collecte de l'utilisation n'est pas encore configurée pour l'espace de travail.
- Il n'y a eu aucune utilisation dans la plage.
- La plage commence avant ce qui est conservé ; elle a donc été raccourcie pour commencer là où l'historique débute. Les données quotidiennes sont conservées 180 jours et les données mensuelles 25 mois.

## Journal de sécurité

Chaque exécution écrit une entrée dans le Journal de sécurité qui consigne le jeu de données, la plage, la table cible, le workflow, l'étape et l'exécution, ainsi que le nombre de lignes écrites.

## Voir aussi

- [Étapes générales](/fr/reference/workflow-steps/general/)
- [Rapports d'utilisation](/fr/administration/access/usage-reports/)
- [Get Workspace Members](/fr/reference/workflow-steps/general/get-workspace-members/)
