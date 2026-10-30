---
title: EXISTS (Lakehouse v1)
description: EXISTS ist eine Bedingung, die zusammen mit einer Unterabfrage verwendet wird und als erfüllt gilt, wenn die Unterabfrage mindestens eine Zeile zurückgibt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/exists.md
---

Die Bedingung EXISTS wird zusammen mit einer Unterabfrage verwendet und gilt als erfüllt, wenn die Unterabfrage mindestens eine Zeile zurückgibt.

## SQL-Syntax

```sql
WHERE EXISTS ( <subquery> );
```

## SQL-Beispiele
```sql
SELECT number FROM numbers(5) AS A WHERE exists (SELECT * FROM numbers(3) WHERE number=1); 
┌────────┐
│ number │
├────────┤
│      0 │
│      1 │
│      2 │
│      3 │
│      4 │
└────────┘
```
