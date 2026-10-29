---
title: FUSE_TIME_TRAVEL_SIZE (Lakehouse v1)
description: FUSE_TIME_TRAVEL_SIZE — calcule la taille de stockage des données historiques (pour le Time travel) des tables.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/16-system-functions/fuse-time-travel-size.md
---

Calcule la taille de stockage des données historiques (pour le Time travel) des tables.

## Syntaxe SQL

```sql
-- Calculate historical data size for all tables in all databases
SELECT ...
FROM fuse_time_travel_size();

-- Calculate historical data size for all tables in a specified database
SELECT ...
FROM fuse_time_travel_size('<database_name>');

-- Calculate historical data size for a specified table in a specified database
SELECT ...
FROM fuse_time_travel_size('<database_name>', '<table_name>'));
```

## Sortie

La fonction renvoie un jeu de résultats comportant les colonnes suivantes :

| Colonne                          | Description                                                                                           |
|----------------------------------|-------------------------------------------------------------------------------------------------------|
| `database_name`                  | Le nom de la base de données où se trouve la table.                                                   |
| `table_name`                     | Le nom de la table.                                                                                   |
| `is_dropped`                     | Indique si la table a été supprimée (`true` pour les tables supprimées, `false` sinon).               |
| `time_travel_size`               | La taille de stockage totale des données historiques (pour le Time travel) de la table, en octets.    |
| `latest_snapshot_size`           | La taille de stockage du dernier instantané de la table, en octets.                                   |
| `data_retention_period_in_hours` | La durée de rétention des données de Time travel, en heures (`NULL` signifie que la politique de rétention par défaut s'applique). |
| `error`                          | Toute erreur rencontrée lors de la récupération de la taille de stockage (`NULL` si aucune erreur ne s'est produite). |

## Exemples SQL

Cet exemple calcule les données historiques de toutes les tables de la base de données `default` :

```sql
SELECT * FROM fuse_time_travel_size('default')

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ database_name │ table_name │ is_dropped │ time_travel_size │ latest_snapshot_size │ data_retention_period_in_hours │       error      │
├───────────────┼────────────┼────────────┼──────────────────┼──────────────────────┼────────────────────────────────┼──────────────────┤
│ default       │ books      │ true       │             2810 │                 1490 │                           NULL │ NULL             │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
