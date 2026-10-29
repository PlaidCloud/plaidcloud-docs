---
title: NULLIF (Lakehouse v1)
description: NULLIF – gibt NULL zurück, wenn zwei Ausdrücke gleich sind.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/nullif.md
---

Gibt NULL zurück, wenn zwei Ausdrücke gleich sind. Andernfalls wird expr1 zurückgegeben. Beide müssen denselben Datentyp haben.

## Analyze-Syntax

```python
func.nullif(<expr1>, <expr2>)
```

## Analyze-Beispiele

```python
func.nullif(0, null) 

┌──────────────────────┐
│ func.nullif(0, null) │
├──────────────────────┤
│                    0 │
└──────────────────────┘
```

## SQL-Syntax

```sql
NULLIF(<expr1>, <expr2>)
```

## SQL-Beispiele

```sql
SELECT NULLIF(0, NULL);

┌─────────────────┐
│ nullif(0, null) │
├─────────────────┤
│               0 │
└─────────────────┘
```
