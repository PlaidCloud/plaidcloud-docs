---
title: Get Workspace Usage
description: Écrivez l'utilisation de l'espace de travail dans une table de projet sous forme d'activité, de membres, de contenu ou de tendances, pour suivre l'adoption ou alimenter une étape en aval.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Description

Écrit l'utilisation de votre espace de travail dans une table de projet. Utilisez-la pour suivre l'adoption dans le temps, pour produire des rapports d'utilisation par service ou par équipe, pour créer vos propres tableaux de bord, ou pour signaler une baisse d'activité dans un workflow planifié. Les chiffres proviennent des mêmes données d'utilisation que les [Rapports d'utilisation](/fr/administration/access/usage-reports/), et chaque jeu de données couvre tous les domaines.

**Activité** et **Membres** contiennent l'identité des membres (ID utilisateur, nom d'utilisateur, e-mail, prénom, nom et groupes de sécurité). La table cible est une table de projet ordinaire, que toute personne ayant accès au projet peut donc lire : traitez-la comme vous traiteriez n'importe quelle liste de membres. Chaque exécution qui écrit la table est consignée dans le Journal de sécurité.

## Configuration

### Données d'utilisation

**Jeu de données** détermine ce que contient chaque ligne. La ligne située sous ce champ nomme les lignes et les colonnes du jeu de données que vous choisissez.

| Jeu de données | Valeur | Une ligne pour chaque | Contient l'identité |
|---|---|---|---|
| **Activité** (par défaut) | `activity` | Jour, membre, action et élément | Oui |
| **Membres** | `members` | Membre, y compris les membres sans activité | Oui |
| **Contenu** | `content` | Tableau de bord, application et notebook, y compris les tableaux de bord et les applications que personne n'a utilisés | Non |
| **Tendances** | `trends` | Jour, semaine et mois de la plage | Non |

Ces valeurs sont celles que contient une étape lorsque vous la créez ou la modifiez via l'API ou un assistant IA. Une étape enregistrée avec un jeu de données absent de cette liste échoue à l'exécution, en nommant les quatre jeux de données : ouvrez-la, choisissez un **Jeu de données** et enregistrez-la. Une étape enregistrée auparavant avec **Membres** ou **Contenu** continue de s'exécuter et écrit les colonnes ci-dessous, et une étape qui était limitée à un domaine couvre désormais tous les domaines.

### Colonnes

Les dates et les jours sont écrits sous forme d'horodatages à minuit UTC.

#### Colonnes des membres

**Activité** et **Membres** incluent ces colonnes :

| Colonne | Contient |
|---|---|
| `user_id` | L'ID du membre. |
| `user_name` | Le nom d'utilisateur du membre. |
| `email` | L'adresse e-mail du membre, en minuscules. |
| `first_name` | Le prénom. |
| `last_name` | Le nom. |
| `is_active` | True lorsque le membre est actif, false lorsqu'il est désactivé. |
| `groups` | Les groupes de sécurité du membre, séparés par `; `. |

`groups` liste les groupes auxquels le membre appartient directement. Les sous-groupes ne sont pas développés.

#### Activité

| Colonne | Contient |
|---|---|
| `day` | Le jour. |
| Les colonnes des membres | Comme ci-dessus. |
| `member` | Le prénom et le nom du membre, ou son nom d'utilisateur lorsque ni l'un ni l'autre n'est défini. |
| `area` | `PlaidCloud app`, `Dashboards`, `Apps` ou `Notebooks`. |
| `action` | `Opened app`, `Opened screen`, `Opened step`, `Saved step`, `Used palette action`, `Viewed dashboard`, `Used chart`, `Opened notebook` ou `Saved notebook`. |
| `item_type` | `App area`, `Screen`, `Step`, `Palette action`, `Dashboard`, `Chart`, `App` ou `Notebook`. |
| `item_id` | L'ID de l'élément. Pour un notebook, son chemin. |
| `item_name` | Le nom de l'élément : un écran ou un domaine de l'application en toutes lettres, comme `Members List` ; le type d'étape ; le nom du tableau de bord, du graphique ou de l'application ; ou le chemin du notebook. Lorsqu'un nom est introuvable, l'ID de l'élément. |
| `events` | Le nombre de fois où le membre l'a fait ce jour-là. |
| `source` | La clé du domaine, telle que la nomment les exportations des [Rapports d'utilisation](/fr/administration/access/usage-reports/). |
| `event` | La clé de l'action, telle que la nomment les exportations. |

`member` et les colonnes des membres dépendent de l'auteur de l'action :

- L'activité qu'aucun membre ne peut se voir attribuer a `Unattributed` dans `member` et des colonnes de membre vides.
- Un membre supprimé depuis ne conserve que `user_id`, et `member` vaut `Deleted user`.
- Tout autre compte, comme un compte de service ou un agent, ne conserve que `user_id`, et `member` correspond à son nom d'utilisateur.

`Used chart` compte une fois par membre et par graphique dans chaque fenêtre de 5 minutes ; il mesure donc l'utilisation, pas les requêtes.

#### Membres

| Colonne | Contient |
|---|---|
| Les colonnes des membres | Comme ci-dessus. |
| `member` | Le prénom et le nom du membre, ou son nom d'utilisateur lorsque ni l'un ni l'autre n'est défini. |
| `created` | Le jour où le membre a été ajouté à l'espace de travail, lorsqu'il est connu. |
| `status` | `Active` lorsque le membre a été actif dans la plage, `Dormant` lorsqu'il a utilisé PlaidCloud auparavant mais pas dans la plage, `Never active` lorsqu'aucune utilisation n'est enregistrée à la fin de la plage. |
| `first_seen` | Le premier jour enregistré où le membre a utilisé PlaidCloud, quelle que soit la plage. |
| `last_seen` | Le dernier jour d'activité du membre dans la plage. |
| `active_days` | Les jours avec activité dans la plage. |
| `events` | Les événements d'activité dans la plage. |
| `active_minutes` | Les minutes d'activité dans la plage. |
| `session_minutes` | Les minutes en session dans la plage. |
| `app_open_minutes` | Les minutes pendant lesquelles le membre a gardé des applications Panel ouvertes dans la plage. Les aperçus Studio ne sont pas comptés. |

Chaque membre a une ligne, y compris les membres désactivés, sauf les membres dont l'utilisation a été effacée. Les comptes de service et les agents ne sont pas listés. Un membre sans activité dans la plage n'a pas de `last_seen`, et ses autres colonnes d'activité sont vides ou à zéro.

#### Contenu

| Colonne | Contient |
|---|---|
| `type` | `Dashboard`, `App` ou `Notebook`. |
| `item_id` | L'ID du tableau de bord ou de l'application, ou le chemin du notebook. |
| `name` | Le nom du tableau de bord ou de l'application, ou le chemin du notebook. Vide lorsque l'élément a été supprimé ou que les noms ne peuvent pas être lus. |
| `deleted` | True lorsque le tableau de bord ou l'application a été supprimé depuis. |
| `unused` | True pour un tableau de bord ou une application que personne n'a utilisé dans la plage. |
| `users` | Les membres qui l'ont utilisé dans la plage. |
| `opens` | Le nombre d'ouvertures dans la plage, y compris les ouvertures qu'aucun membre ne peut se voir attribuer. |
| `last_used` | Le dernier jour d'utilisation dans la plage. Pour un élément inutilisé, le dernier jour où il a été ouvert avant la fin de la plage, ou vide. |
| `app_open_minutes` | Les minutes pendant lesquelles une application Panel était ouverte dans la plage. Vide pour les tableaux de bord, les notebooks et les applis Dash et WASM. |

Chaque chemin de notebook a sa propre ligne. Les lignes listent d'abord ce qui a été utilisé, en commençant par le plus d'utilisateurs, puis les tableaux de bord et les applications que personne n'a utilisés. Il s'agit des tableaux de bord publiés et des applications qui existaient déjà au début de la plage. Ils ne sont listés que si la plage commence dans les données quotidiennes conservées, si l'utilisation de ce type d'élément était déjà collectée à ce moment-là et si les noms peuvent être lus. Les aperçus Studio des applications sont exclus.

#### Tendances

| Colonne | Contient |
|---|---|
| `period` | `Day`, `Week` ou `Month`. |
| `period_start` | Le premier jour de la période. Les semaines commencent le lundi. |
| `active_members` | Les membres actifs dans la période, au sein de la plage. |
| `events` | Les événements d'activité dans la période. |
| `active_minutes` | Les minutes d'activité dans la période. |
| `session_minutes` | Les minutes en session dans la période. |
| `active_members_7d` | Sur une ligne `Day`, les membres actifs au cours des 7 jours se terminant ce jour-là. |
| `active_members_28d` | Sur une ligne `Day`, les membres actifs au cours des 28 jours se terminant ce jour-là. |
| `stickiness` | Sur une ligne `Day`, `active_members` divisé par `active_members_28d`. |
| `complete` | False pour aujourd'hui, pour une semaine ou un mois qui contient aujourd'hui, et pour une semaine ou un mois que la plage coupe. |

Chaque jour de la plage, à partir du début des données quotidiennes conservées, a une ligne, même sans utilisation, de même que chaque semaine et chaque mois dans lesquels tombent ces jours. `active_members_7d`, `active_members_28d` et `stickiness` sont vides sur les lignes `Week` et `Month`, et sur une ligne `Day` dont les 7 ou 28 jours remontent avant les données quotidiennes conservées. Un mois qui commence avant les données quotidiennes conservées et entièrement compris dans la plage provient des synthèses mensuelles : il a `active_members` mais des événements et des minutes vides, et `complete` indique si la synthèse couvrait tout le mois.

### Exemple : minutes actives par service

**Activité** et **Membres** contiennent l'`email` du membre, en minuscules, ce qui vous permet de les joindre à une table de votre choix, comme une table RH ou une table de référence de l'organisation, et de produire un rapport par service.

1. Ajoutez une étape **Get Workspace Usage** avec **Jeu de données** défini sur **Membres**, et une table cible telle que `usage_members`.
2. Ajoutez une étape **Table : jointure interne** qui joint `usage_members` à votre table d'organisation là où les colonnes `email` en minuscules correspondent. Conservez le service issu de votre table, ainsi que les colonnes `active_minutes` et `events` de `usage_members`.
3. Dans la même étape, agrégez par service et faites la somme de `active_minutes`.

Le résultat donne les minutes actives par service. Les membres absents de votre table d'organisation disparaissent d'une jointure interne ; utilisez donc une jointure gauche si vous souhaitez les voir. Répétez l'opération avec une seconde étape sur **Activité** et faites la somme de `events` par service et par `item_name` pour savoir qui utilise quels tableaux de bord et quelles applications.

### Plage de dates

**Plage** détermine les jours à lire :

| Plage | Valeur | Lit |
|---|---|---|
| **Nombre de derniers jours** (30 par défaut) | `last_days` | Les jours les plus récents, aujourd'hui inclus. |
| **Mois précédent** | `previous_month` | Le dernier mois calendaire complet. |
| **Cumul du mois** | `month_to_date` | Du premier jour du mois en cours jusqu'à aujourd'hui. |
| **Entre deux dates** | `dates` | De **Date de début** à **Date de fin**. Laissez **Date de fin** vide pour lire jusqu'à aujourd'hui. |

Les jours et les dates sont en UTC. **Jours** accepte un nombre entier. **Date de début** et **Date de fin** acceptent une date au format `YYYY-MM-DD` ou une [variable](/fr/guides/workflows/manage-workflow-variables/) telle que `{report_start}`. Le début ne doit pas être postérieur à la fin.

Les données quotidiennes sont conservées 180 jours et les synthèses mensuelles 25 mois.

### Cible de l'utilisation

**Table cible** reçoit le résultat. L'étape remplace tout ce que la table contenait, et écrit toujours les colonnes du jeu de données, même lorsqu'il n'y a aucune ligne.

## Avertissements

Ces cas ne font pas échouer l'étape. Elle se termine avec l'avertissement et remplace quand même la table, avec les colonnes du jeu de données :

| Avertissement | Signification |
|---|---|
| "Usage data is not available yet: the usage database has not been set up on this workspace." | La collecte de l'utilisation n'est pas encore configurée pour l'espace de travail. |
| "Usage data is not available right now: the usage database could not be reached." | Les données d'utilisation n'ont pas pu être lues. Réexécutez l'étape plus tard. |
| "No usage from *start* to *end*." | Il n'y a eu aucune utilisation dans la plage. |
| "Usage before *date* isn't kept, so the range was clipped to start there." | La plage commence avant les données quotidiennes conservées ; l'activité est donc comptée à partir de *date*. **Tendances** contient toujours les mois entiers qui précèdent, issus des synthèses mensuelles. |
| "This took too long to compute: narrow the date range." | La lecture a dépassé le délai imparti ; la table n'a donc aucune ligne. Choisissez une plage plus courte. |
| "Some names are unavailable right now, so those items are named by their id." | **Activité** uniquement. Certains noms de tableaux de bord, de graphiques ou d'applications n'ont pas pu être lus ; `item_name` contient donc l'ID. |
| "Members could not be read right now, so they are named by their id." | **Activité** uniquement. La liste des membres n'a pas pu être lue ; `member` contient donc l'ID du membre et, parmi les colonnes des membres, seul `user_id` est renseigné. |
| "Names are unavailable right now, so items nobody used are not listed." | **Contenu** uniquement. Les noms des tableaux de bord ou des applications n'ont pas pu être lus ; seuls les éléments utilisés sont donc listés. |
| "Activity before *date* isn't kept, so items nobody used in this range can't be listed." | **Contenu** uniquement. La plage commence avant les données quotidiennes conservées ; seuls les éléments utilisés sont donc listés. |

Lorsque la liste des membres ne peut pas être lue, **Membres** échoue à la place et laisse la table cible telle qu'elle était.

## Journal de sécurité

Chaque exécution qui écrit la table ajoute une entrée au Journal de sécurité qui consigne le jeu de données, la plage, la table cible et son projet, le workflow, l'étape et l'exécution, le nombre de lignes écrites et, pour **Activité** et **Membres**, le fait que les lignes contiennent l'identité des membres.

## Voir aussi

- [Étapes générales](/fr/reference/workflow-steps/general/)
- [Rapports d'utilisation](/fr/administration/access/usage-reports/)
- [Get Workspace Members](/fr/reference/workflow-steps/general/get-workspace-members/)
