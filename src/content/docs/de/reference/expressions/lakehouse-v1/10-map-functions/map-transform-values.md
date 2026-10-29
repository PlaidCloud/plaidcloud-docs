---
title: MAP_TRANSFORM_VALUES (Lakehouse v1)
description: MAP_TRANSFORM_VALUES — wendet mit einem Lambda-Ausdruck eine Transformation auf jeden Wert einer Map an.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-values.md
---

Wendet mit einem Lambda-Ausdruck eine Transformation auf jeden Wert einer Map an.

## SQL-Syntax

```sql
MAP_TRANSFORM_VALUES(<map>, (<key>, <value>) -> <value_transformation>)
```

## Rückgabetyp

Gibt eine Map mit denselben Schlüsseln wie die Eingabe-Map zurück, deren Werte jedoch gemäß der angegebenen Lambda-Transformation geändert wurden.

## SQL-Beispiele

Dieses Beispiel senkt den Preis jedes Produkts um 10 %, während die Produkt-IDs (Schlüssel) unverändert bleiben:

```sql
SELECT MAP_TRANSFORM_VALUES({101: 100.0, 102: 150.0, 103: 200.0}, (product_id, price) -> price * 0.9) AS discounted_prices;

┌───────────────────────────────────┐
│         discounted_prices         │
├───────────────────────────────────┤
│ {101:90.00,102:135.00,103:180.00} │
└───────────────────────────────────┘
```
