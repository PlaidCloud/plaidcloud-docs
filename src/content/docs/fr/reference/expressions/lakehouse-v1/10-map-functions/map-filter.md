---
title: MAP_FILTER (Lakehouse v1)
description: MAP_FILTER — filtre les paires clé-valeur d'un map à l'aide d'une expression lambda qui définit la condition.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-filter.md
---

Filtre les paires clé-valeur d'un map à l'aide d'une expression lambda qui définit la condition.

## Syntaxe SQL

```sql
MAP_FILTER(<map>, (<key>, <value>) -> <condition>)
```

## Type de retour

Renvoie un map qui ne comprend que les paires clé-valeur satisfaisant la condition définie par l'expression lambda.

## Exemples SQL

Cet exemple renvoie un map contenant uniquement les produits dont le stock est inférieur à 10 :

```sql
SELECT MAP_FILTER({101:15, 102:8, 103:12, 104:5}, (product_id, stock) -> (stock < 10)) AS low_stock_products;

┌────────────────────┐
│ low_stock_products │
├────────────────────┤
│ {102:8,104:5}      │
└────────────────────┘
```
