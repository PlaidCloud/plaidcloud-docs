---
title: MAP_TRANSFORM_VALUES (Lakehouse v1)
description: MAP_TRANSFORM_VALUES — applique une transformation à chaque valeur d'un map à l'aide d'une expression lambda.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-values.md
---

Applique une transformation à chaque valeur d'un map à l'aide d'une expression lambda.

## Syntaxe SQL

```sql
MAP_TRANSFORM_VALUES(<map>, (<key>, <value>) -> <value_transformation>)
```

## Type de retour

Renvoie un map ayant les mêmes clés que le map en entrée, mais dont les valeurs sont modifiées selon la transformation lambda indiquée.

## Exemples SQL

Cet exemple réduit le prix de chaque produit de 10 %, tandis que les identifiants de produit (les clés) restent inchangés :

```sql
SELECT MAP_TRANSFORM_VALUES({101: 100.0, 102: 150.0, 103: 200.0}, (product_id, price) -> price * 0.9) AS discounted_prices;

┌───────────────────────────────────┐
│         discounted_prices         │
├───────────────────────────────────┤
│ {101:90.00,102:135.00,103:180.00} │
└───────────────────────────────────┘
```
