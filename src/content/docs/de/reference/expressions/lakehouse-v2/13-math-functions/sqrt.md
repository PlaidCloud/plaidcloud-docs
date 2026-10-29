---
title: SQRT (Lakehouse v2)
description: SQRT – gibt die Quadratwurzel einer Zahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sqrt.md
---

Gibt die Quadratwurzel einer Zahl zurück.

## Analyze-Syntax

```python
func.sqrt(<x>)
```

## Analyze-Beispiele

```python
func.sqrt(144)

┌──────┐
│ 12.0  │
└──────┘
```

## SQL-Syntax

```sql
SQRT(<x>)
```

## SQL-Beispiele

```sql
SELECT SQRT(144);

┌──────┐
│ 12.0  │
└──────┘
```
