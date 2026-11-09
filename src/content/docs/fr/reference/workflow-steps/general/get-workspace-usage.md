---
title: Get Workspace Usage (étape)
description: Écrivez les totaux d'utilisation de l'espace de travail issus des Rapports d'utilisation dans une table de projet, par jour ou par mois, pour suivre l'adoption sous forme de graphique ou alimenter une étape en aval.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Description

Écrit dans une table de projet la manière dont votre espace de travail est utilisé. Utilisez-la pour suivre l'adoption dans le temps, produire des rapports d'utilisation par service ou par équipe, créer vos propres tableaux de bord ou signaler une baisse d'activité dans un workflow planifié. Les chiffres sont les mêmes que ceux affichés par les [Rapports d'utilisation](/fr/administration/access/usage-reports/).

Trois jeux de données ne contiennent que des totaux : aucune ligne ne désigne un membre, et les chemins de notebook sont remplacés par `*`. Les quatre autres (**Membres**, **Quotidien par membre**, **Contenu** et **Contenu par membre**) sont conçus pour le reporting. **Membres**, **Quotidien par membre** et **Contenu par membre** contiennent l'identité des membres (ID utilisateur, nom d'utilisateur, e-mail, prénom, nom et groupes de sécurité) ; traitez donc la table cible comme vous le feriez pour n'importe quelle liste de membres. Chaque exécution de l'étape est enregistrée dans le Journal de sécurité.

## Configuration

### Données d'utilisation

**Jeu de données** détermine ce que contient chaque ligne :

| Jeu de données | Une ligne pour chaque | Contient l'identité |
|---|---|---|
| **Quotidien par élément** | Jour, domaine, événement et sujet | Non |
| **Mensuel par élément** | Mois, domaine, événement et sujet | Non |
| **Totaux mensuels** (par défaut) | Mois et domaine | Non |
| **Membres** | Personne de l'espace de travail | Oui |
| **Quotidien par membre** | Personne, jour et domaine | Oui |
| **Contenu** | Tableau de bord, application ou notebook | Non |
| **Contenu par membre** | Personne et élément | Oui |

**Domaine** limite les lignes à un domaine : **Application PlaidCloud**, **Tableaux de bord**, **Applications**, **Visites d'applications** ou **Notebooks**. Laissez **Tous les domaines** pour les inclure tous.

### Colonnes

#### Quotidien par élément

`day`, `source`, `event`, `subject`, `events`.

#### Mensuel par élément

`month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial`.

#### Totaux mensuels

`month`, `source`, `active_users`, `coverage_start`, `partial`.

`partial` est vrai pour un mois que l'historique ne couvre pas entièrement, et `coverage_start` correspond à la date de début de la collecte. Un mois est inclus une fois qu'il est clos et stabilisé, ce qui prend 3 jours.

#### Colonnes de membre

**Membres**, **Quotidien par membre** et **Contenu par membre** commencent par les mêmes sept colonnes :

| Colonne | Contient |
|---|---|
| `user_id` | L'ID du membre. |
| `user_name` | Le nom d'utilisateur du membre. |
| `email` | L'adresse e-mail du membre, en minuscules. |
| `first_name` | Le prénom. |
| `last_name` | Le nom. |
| `is_active` | Vrai lorsque le membre est actif, faux lorsqu'il est désactivé. |
| `groups` | Les groupes de sécurité du membre, séparés par `; `. |

`groups` ne répertorie que les groupes de premier niveau. Les sous-groupes ne sont pas développés.

#### Membres

Les colonnes de membre, puis :

| Colonne | Contient |
|---|---|
| `first_seen` | Le premier jour où le membre a utilisé PlaidCloud, quelle que soit la période. |
| `last_seen` | Le dernier jour d'activité du membre dans la période. |
| `active_days` | Les jours d'activité dans la période. |
| `events` | Les événements d'activité dans la période. |
| `active_minutes` | Les minutes d'activité. Les minutes qui se chevauchent entre domaines ne sont comptées qu'une fois. |
| `session_minutes` | Les minutes en session. |
| `app_open_minutes` | Les minutes pendant lesquelles le membre a gardé des applications Panel ouvertes. |

Chaque personne de l'espace de travail a une ligne. Un membre sans activité dans la période a des valeurs vides après `groups`. Les totaux correspondent à ceux des [Rapports d'utilisation](/fr/administration/access/usage-reports/), à l'exception des membres supprimés depuis.

#### Quotidien par membre

Les colonnes de membre, puis `day`, `source` (le domaine), `events`, `active_minutes`, `session_minutes`, `first_at` et `last_at` (les heures de première et de dernière activité de la journée).

#### Contenu

| Colonne | Contient |
|---|---|
| `type` | `dashboard`, `panel_app`, `wasm_app` ou `notebook`. |
| `subject` | L'ID de l'élément. Tous les notebooks partagent une seule ligne, avec `*` ici. |
| `name` | Le nom de l'élément, ou `*` pour les notebooks. |
| `deleted` | Vrai lorsque l'élément a été supprimé depuis. |
| `users` | Les membres qui l'ont ouvert. |
| `opens` | Le nombre d'ouvertures. |
| `last_used` | La date de dernière utilisation. |
| `app_open_minutes` | Les minutes pendant lesquelles des applications Panel étaient ouvertes. |

#### Contenu par membre

Les colonnes de membre, puis `type`, `subject`, `name` (comme dans **Contenu**), `opens` (le nombre de fois où ce membre a ouvert l'élément) et `last_day` (le dernier jour d'utilisation du membre).

### Remarques sur les jeux de données de membres

- L'activité des agents, des comptes de service et des membres supprimés depuis a des colonnes d'identité vides. Un membre supprimé conserve le `user_id` et rien d'autre.
- Les ouvertures dans **Contenu** peuvent dépasser la somme des ouvertures dans **Contenu par membre**. La différence correspond aux ouvertures qui ne peuvent pas être attribuées à un membre, comme les consultations intégrées ou invitées d'un tableau de bord. **Contenu** les compte, et **Contenu par membre** ne le peut pas.

### Exemple : minutes d'activité par service

**Membres** et **Contenu par membre** contiennent l'`email` du membre, en minuscules, ce qui vous permet de les joindre à une table de votre choix, par exemple une table de référence RH ou d'organisation, et de produire un rapport par service.

1. Ajoutez une étape **Get Workspace Usage** avec **Jeu de données** défini sur **Membres**, et une table cible telle que `usage_members`.
2. Ajoutez une étape **Table : jointure interne** qui joint `usage_members` à votre table d'organisation lorsque les colonnes `email` en minuscules correspondent. Conservez le service issu de votre table et les colonnes `active_minutes` et `events` de `usage_members`.
3. Dans la même étape, agrégez par service et additionnez `active_minutes`.

Le résultat est le nombre de minutes d'activité par service. Les membres qui ne figurent pas dans votre table d'organisation sont exclus d'une jointure interne ; utilisez donc une jointure gauche si vous souhaitez les voir. Répétez l'opération avec une seconde étape sur **Contenu par membre** et additionnez `opens` par service pour savoir qui utilise quels tableaux de bord et applications.

### Plage de dates

**Période** détermine les jours à lire :

- **Nombre de derniers jours** (30 par défaut) lit les jours les plus récents, aujourd'hui inclus.
- **Mois précédent** lit le dernier mois calendaire complet.
- **Cumul du mois** lit du premier jour du mois en cours jusqu'à aujourd'hui.
- **Entre deux dates** lit de **Date de début** à **Date de fin**. Laissez **Date de fin** vide pour lire jusqu'à aujourd'hui.

Les jours et les dates sont en UTC. **Jours**, **Date de début** et **Date de fin** acceptent une [variable](/fr/guides/workflows/manage-workflow-variables/) telle que `{report_start}`, ainsi qu'un nombre ou une date au format `YYYY-MM-DD`. Le début ne doit pas être postérieur à la fin.

### Cible d'utilisation

**Table cible** reçoit le résultat. L'étape remplace tout ce que contenait la table et écrit toujours les colonnes du jeu de données, même lorsqu'il n'y a aucune ligne.

## Avertissements

Ces cas ne font pas échouer l'étape. Elle se termine avec un avertissement qui indique ce qui s'est passé, et écrit tout de même la table :

- La collecte d'utilisation n'est pas encore configurée pour l'espace de travail.
- Il n'y a eu aucune utilisation dans la période.
- La période commence avant ce qui est conservé ; elle a donc été tronquée pour commencer là où l'historique débute. Les données quotidiennes sont conservées 180 jours et les données mensuelles 25 mois.

## Journal de sécurité

Chaque exécution écrit une entrée dans le Journal de sécurité qui consigne le jeu de données, la période, la table cible, le workflow, l'étape et l'exécution, ainsi que le nombre de lignes écrites.

## Voir aussi

- [Étapes générales](/fr/reference/workflow-steps/general/)
- [Rapports d'utilisation](/fr/administration/access/usage-reports/)
- [Get Workspace Members](/fr/reference/workflow-steps/general/get-workspace-members/)
