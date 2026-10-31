---
title: "TM1 : interroger un cube"
description: Lisez les données d'un cube sur un serveur IBM TM1 / Planning Analytics à partir d'une vue enregistrée ou d'une requête MDX, appliquez éventuellement une tranche de point de vue et enregistrez le résultat dans une table, en direct dans le cloud via REST, avec un aperçu avant l'enregistrement.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-query.md
---

## Description

Lit les données d'un cube IBM **TM1 / Planning Analytics** via votre [connexion TM1](/fr/guides/connections/tm1/), soit en exécutant une **vue** enregistrée, soit en écrivant une requête **MDX**. Un point de vue (POV) peut fixer des membres de dimension supplémentaires en plus de ce que la vue ou la requête MDX fixe déjà. Le jeu de cellules renvoyé est enregistré dans une table de projet (schéma à la lecture), avec des colonnes de dimension et une colonne de mesure `Value`, créées à partir des axes de la requête elle-même.

Cette étape apparaît dans le menu des étapes sous **IBM TM1 / Planning Analytics**.

L'étape accède à TM1 **en direct dans le cloud** via son API REST : aucun agent local n'intervient, et il n'en existe pas encore pour cette étape.

## Configuration

### Source et cible

| Champ | Obligatoire | Remarques |
|---|---|---|
| Connexion TM1 | Oui | La [connexion TM1](/fr/guides/connections/tm1/) à utiliser pour la lecture. |
| Environment | Oui | L'environnement de la connexion. |
| Database | Oui | La base de données TM1 (instance) à interroger. Par défaut, la Base de données par défaut de la connexion si elle est définie. |
| Cube | Oui | Le cube TM1 à interroger. Détecté en direct depuis la base de données connectée, ou saisi à la main. |
| Table cible | Oui | La table de projet dans laquelle le jeu de cellules renvoyé est enregistré. |

### Tranche

| Champ | Obligatoire | Remarques |
|---|---|---|
| Mode de source | Oui | `By View` (par défaut) exécute une vue TM1 enregistrée. `By MDX` exécute une requête MDX brute que vous écrivez. |
| View | Avec By View | La vue de cube TM1 enregistrée à exécuter. Détectée en direct une fois le cube choisi, ou saisie à la main. |
| MDX | Avec By MDX | La requête MDX à exécuter sur le cube. |

### Point de vue

Fixez un membre par dimension pour borner la tranche au-delà de ce que la vue ou la requête MDX fixe déjà, ce qui est utile pour une extraction incrémentale (voir ci-dessous). Ajoutez une ligne de dimension, choisissez la dimension, puis saisissez le membre. Une valeur de membre peut être un littéral (`Jan-2026`) ou un jeton `{variable}` résolu à l'exécution à partir des variables du workflow, avec la même substitution que celle appliquée au champ MDX lui-même. Laissez le point de vue vide pour une simple lecture de vue ou de requête MDX. Appliquer un point de vue avec `By View` n'est pas pris en charge : utilisez `By MDX` si vous en avez besoin.

### Options

| Champ | Par défaut | Remarques |
|---|---|---|
| Supprimer les cellules nulles/vides | Désactivé | Supprime les cellules dont la valeur est exactement le nombre `0` **après** leur récupération. Cela n'économise aucune bande passante et, dans un cube de planification où un `0` saisi est un fait réel, l'écarte. Préférez supprimer les zéros dans la requête elle-même (`NON EMPTY` dans votre MDX, ou le paramètre de suppression de la vue enregistrée) afin que TM1 ne les calcule jamais. |
| Limite de lignes | 250 000 | Plafonne le nombre de cellules renvoyées. Laissez vide pour utiliser le plafond par défaut de 250 000 ; augmentez-le ou réduisez-le explicitement, car une Limite de lignes non définie n'est pas illimitée. Une requête qui dépasse la limite effective est refusée au lieu d'être tronquée silencieusement. |

## Extractions incrémentales

TM1 n'offre aucun suivi des modifications intégré : il n'existe donc pas d'appel du type « donne-moi uniquement ce qui a changé depuis la dernière fois ». Le principe consiste plutôt à **découper par période (ou par version)** à chaque exécution : fixez `Period` dans le point de vue sur une variable de workflow `{period}` plutôt que sur un nom de membre littéral, afin que chaque exécution substitue sa propre période cible et récupère les données d'une seule période au lieu de tout le cube. Combinez cela avec un workflow planifié et une variable qui avance à chaque exécution pour construire un historique incrémental période par période.

## Aperçu

Avant l'enregistrement, **Aperçu** exécute la tranche actuelle sur TM1 et affiche les premières lignes ainsi que le nombre de cellules, plafonnés à une petite limite de lignes indépendante de la Limite de lignes configurée dans l'étape.

## Lorsque Value est enregistrée en texte

Une dimension de mesures TM1 contient couramment des éléments numériques (`Sales`, `Cost`) à côté d'éléments de type chaîne (`Comment`, `Status`) dans la même dimension. Une tranche qui couvre les deux enregistre la colonne `Value` en texte : une colonne n'a qu'un seul type physique, et une seule cellule non numérique dans la tranche suffit à le déterminer.

Ce comportement est correct : mettre les cellules de type chaîne à null ferait perdre des données, faire échouer la requête bloquerait un cube légitime, et scinder en deux colonnes ferait dépendre le schéma des données renvoyées. À la place, l'étape le signale. Elle émet un avertissement qui nomme la colonne, l'ampleur du phénomène et les éléments responsables, par exemple :

> Column Value landed as text: 3 of 4,812 cells are non-numeric (text or boolean), and a column can only have one type. The non-numeric cells come from element Comment. Exclude that element from the slice, or query it separately, to keep this column numeric.

**Aperçu** affiche le même détail avant l'enregistrement, et le sélecteur de membres du point de vue indique le type TM1 de chaque élément (Numeric, String ou Consolidated) pour qu'un élément de type chaîne soit visible avant de le fixer. Fixer un élément de type chaîne dans le point de vue n'est pas bloqué, car c'est une façon légitime de lire une mesure textuelle, mais cela enregistre toute la colonne `Value` en texte, puisque la mesure se trouve dans le POV et non sur un axe ; dans ce cas, l'avertissement indique les nombres sans nommer d'élément, car tous les membres des axes sont également non numériques et aucun ne distingue la tranche.

Pour conserver `Value` en numérique, excluez l'élément de type chaîne de la tranche, ou interrogez séparément les mesures de type chaîne et les mesures numériques.

## Limites des capacités

| Limite | Signification |
|---|---|
| Lecture seule | Lit les données de cube depuis TM1. Pas de réécriture, pas d'exécution de processus TI. |
| Cloud direct uniquement | Pas encore de chemin par agent PlaidLink local pour cette étape : le serveur TM1 doit disposer d'un chemin réseau que PlaidCloud peut atteindre directement. |
| Pas de suivi des modifications | TM1 n'expose aucune API de delta ou de modifications depuis une date. Découpez plutôt par période ou par version à chaque exécution (voir Extractions incrémentales ci-dessus). |
| Pas d'importation de dimension/hiérarchie | Cette étape lit les données de cube. L'importation des hiérarchies de dimension TM1 en tant que dimensions PlaidCloud n'est pas encore disponible. |

## Voir aussi

- [Se connecter à TM1 (guide)](/fr/guides/connections/tm1/) : créez la connexion et construisez une requête.
- [Connecteur TM1](/fr/reference/connectors/rest/tm1/) : référence des champs de connexion.
- [Étapes IBM TM1 / Planning Analytics](/fr/reference/workflow-steps/ibm-planning-analytics/)
