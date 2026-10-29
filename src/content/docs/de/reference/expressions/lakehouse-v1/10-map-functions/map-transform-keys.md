---
title: MAP_TRANSFORM_KEYS (Lakehouse v1)
description: MAP_TRANSFORM_KEYS — wendet mit einem Lambda-Ausdruck eine Transformation auf jeden Schlüssel einer Map an.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-transform-keys.md
---

Wendet mit einem Lambda-Ausdruck eine Transformation auf jeden Schlüssel einer Map an.

## SQL-Syntax

```sql
MAP_TRANSFORM_KEYS(<map>, (<key>, <value>) -> <key_transformation>)
```

## Rückgabetyp

Gibt eine Map mit denselben Werten wie die Eingabe-Map zurück, deren Schlüssel jedoch gemäß der angegebenen Lambda-Transformation geändert wurden.

## SQL-Beispiele

Dieses Beispiel addiert 1.000 zu jeder Produkt-ID und erstellt so eine neue Map mit aktualisierten Schlüsseln, wobei die zugehörigen Preise gleich bleiben:

```sql
SELECT MAP_TRANSFORM_KEYS({101: 29.99, 102: 45.50, 103: 15.00}, (product_id, price) -> product_id + 1000) AS updated_product_ids;

┌────────────────────────────────────┐
│         updated_product_ids        │
├────────────────────────────────────┤
│ {1101:29.99,1102:45.50,1103:15.00} │
└────────────────────────────────────┘
```
