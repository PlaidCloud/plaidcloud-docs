---
title: NEGATIVE (Lakehouse v2)
description: NEGATIVE – gibt die Negation einer Zahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/negative.md
---

Gibt die Negation einer Zahl zurück.

## Analyze-Syntax

```python
func.negative(<x>)
```

## Analyze-Beispiele

```python
func.negative(5)

┌────┐
│ -5  │
└────┘
```

## SQL-Syntax

```sql
NEGATIVE(<x>)
```

## SQL-Beispiele

```sql
SELECT NEGATIVE(5);

┌────┐
│ -5  │
└────┘
```
