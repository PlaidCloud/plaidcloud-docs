---
title: ROUND (Lakehouse v2)
description: ROUND – rundet eine Zahl auf eine angegebene Anzahl von Dezimalstellen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/round.md
---

Rundet eine Zahl auf eine angegebene Anzahl von Dezimalstellen.

## Analyze-Syntax

```python
func.round(<x>[, <d>])
```

## Analyze-Beispiele

```python
func.round(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## SQL-Syntax

```sql
ROUND(<x>[, <d>])
```

## SQL-Beispiele

```sql
SELECT ROUND(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
