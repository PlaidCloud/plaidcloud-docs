---
title: MAP_TRANSFORM_KEYS (Lakehouse v1)
description: MAP_TRANSFORM_KEYS — applique une transformation à chaque clé d'un map à l'aide d'une expression lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-keys.md
---

Applique une transformation à chaque clé d'un map à l'aide d'une expression lambda.

## Syntaxe SQL

```sql
MAP_TRANSFORM_KEYS(<map>, (<key>, <value>) -> <key_transformation>)
```

## Type de retour

Renvoie un map ayant les mêmes valeurs que le map en entrée, mais dont les clés sont modifiées selon la transformation lambda indiquée.

## Exemples SQL

Cet exemple ajoute 1 000 à chaque identifiant de produit et crée ainsi un nouveau map aux clés mises à jour, en conservant les mêmes prix :

```sql
SELECT MAP_TRANSFORM_KEYS({101: 29.99, 102: 45.50, 103: 15.00}, (product_id, price) -> product_id + 1000) AS updated_product_ids;

┌────────────────────────────────────┐
│         updated_product_ids        │
├────────────────────────────────────┤
│ {1101:29.99,1102:45.50,1103:15.00} │
└────────────────────────────────────┘
```
