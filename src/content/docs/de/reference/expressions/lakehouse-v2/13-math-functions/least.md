---
title: LEAST (Lakehouse v2)
description: LEAST – gibt den kleinsten Wert aus einer Liste von Werten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/least.md
---

Gibt den kleinsten Wert aus einer Liste von Werten zurück.

## Analyze-Syntax

```python
func.least(<val1>, <val2>[, ...])
```

## Analyze-Beispiele

```python
func.least(3, 7, 1, 9, 4)

┌───┐
│ 1  │
└───┘
```

## SQL-Syntax

```sql
LEAST(<val1>, <val2>[, ...])
```

## SQL-Beispiele

```sql
SELECT LEAST(3, 7, 1, 9, 4);

┌───┐
│ 1  │
└───┘
```
