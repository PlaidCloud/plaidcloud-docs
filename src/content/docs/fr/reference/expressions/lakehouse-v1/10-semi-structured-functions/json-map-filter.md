---
title: JSON_MAP_FILTER (Lakehouse v1)
description: JSON_MAP_FILTER — filtre les paires clé-valeur d'un objet JSON selon une condition donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-filter.md
---

Filtre les paires clé-valeur d'un objet JSON selon une condition donnée, définie à l'aide d'une expression lambda.

## Syntaxe SQL

```sql
JSON_MAP_FILTER(<json_object>, (<key>, <value>) -> <condition>)
```

## Type de retour

Renvoie un objet JSON ne contenant que les paires clé-valeur qui satisfont la condition spécifiée.

## Exemples SQL

Cet exemple extrait uniquement la paire clé-valeur `"status": "active"` de l'objet JSON et écarte les autres champs :

```sql
SELECT JSON_MAP_FILTER('{"status":"active", "user":"admin", "time":"2024-11-01"}'::VARIANT, (k, v) -> k = 'status') AS filtered_metadata;

┌─────────────────────┐
│  filtered_metadata  │
├─────────────────────┤
│ {"status":"active"} │
└─────────────────────┘
```
