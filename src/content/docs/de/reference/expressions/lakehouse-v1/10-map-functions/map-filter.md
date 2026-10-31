---
title: MAP_FILTER (Lakehouse v1)
description: MAP_FILTER — filtert Schlüssel-Wert-Paare einer Map mit einem Lambda-Ausdruck, der die Bedingung definiert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-map-functions/map-filter.md
---

Filtert Schlüssel-Wert-Paare einer Map mit einem Lambda-Ausdruck, der die Bedingung definiert.

## SQL-Syntax

```sql
MAP_FILTER(<map>, (<key>, <value>) -> <condition>)
```

## Rückgabetyp

Gibt eine Map zurück, die nur die Schlüssel-Wert-Paare enthält, welche die durch den Lambda-Ausdruck festgelegte Bedingung erfüllen.

## SQL-Beispiele

Dieses Beispiel gibt eine Map zurück, die nur die Produkte mit einem Lagerbestand unter 10 enthält:

```sql
SELECT MAP_FILTER({101:15, 102:8, 103:12, 104:5}, (product_id, stock) -> (stock < 10)) AS low_stock_products;

┌────────────────────┐
│ low_stock_products │
├────────────────────┤
│ {102:8,104:5}      │
└────────────────────┘
```
