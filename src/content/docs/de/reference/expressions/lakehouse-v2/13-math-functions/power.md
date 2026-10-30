---
title: POWER (Lakehouse v2)
description: POWER – gibt eine Zahl potenziert mit einer anderen Zahl zurück. Alias für `POW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/power.md
---

Gibt eine Zahl potenziert mit einer anderen Zahl zurück. Alias für `POW`.

## Analyze-Syntax

```python
func.power(<x>, <y>)
```

## Analyze-Beispiele

```python
func.power(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## SQL-Syntax

```sql
POWER(<x>, <y>)
```

## SQL-Beispiele

```sql
SELECT POWER(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
