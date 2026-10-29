---
title: JSON_MAP_TRANSFORM_KEYS (Lakehouse v1)
description: JSON_MAP_TRANSFORM_KEYS — applique une transformation à chaque clé d'un objet JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/json-map-transform-keys.md
---

Applique une transformation à chaque clé d'un objet JSON à l'aide d'une expression lambda.

## Syntaxe SQL

```sql
JSON_MAP_TRANSFORM_KEYS(<json_object>, (<key>, <value>) -> <key_transformation>)
```

## Type de retour

Renvoie un objet JSON ayant les mêmes valeurs que l'objet JSON en entrée, mais dont les clés sont modifiées selon la transformation lambda spécifiée.

## Exemples SQL

Cet exemple ajoute « _v1 » à chaque clé, ce qui crée un nouvel objet JSON dont les clés sont modifiées :

```sql
SELECT JSON_MAP_TRANSFORM_KEYS('{"name":"John", "role":"admin"}'::VARIANT, (k, v) -> CONCAT(k, '_v1')) AS versioned_metadata;

┌──────────────────────────────────────┐
│          versioned_metadata          │
├──────────────────────────────────────┤
│ {"name_v1":"John","role_v1":"admin"} │
└──────────────────────────────────────┘
```
