---
title: GREATEST (Lakehouse v1)
description: GREATEST – gibt den größten Wert aus einer Menge von Werten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/greatest.md
---

Gibt den größten Wert aus einer Menge von Werten zurück.

## Analyze-Syntax

```python
func.greatest(<value1>, <value2> ...)
```

## Analyze-Beispiele

```python
func.greatest((5, 9, 4))

┌──────────────────────────┐
│ func.greatest((5, 9, 4)) │
├──────────────────────────┤
│                        9 │
└──────────────────────────┘
```

## SQL-Syntax

```sql
GREATEST(<value1>, <value2> ...)
```

## SQL-Beispiele

```sql
SELECT GREATEST(5, 9, 4);

┌───────────────────┐
│ greatest(5, 9, 4) │
├───────────────────┤
│                 9 │
└───────────────────┘
```
