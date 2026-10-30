---
title: DLOG1 (Lakehouse v2)
description: DLOG1 — alias funkcji `LN`. Zobacz [LN](../ln/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog1.md
---

Alias funkcji `LN`. Zobacz [LN](../ln/).

## Składnia Analyze

```python
func.dlog1(2.718281828459045)
```

## Przykłady Analyze

```python
func.dlog1(2.718281828459045)

┌─────┐
│ 1.0 │
└─────┘
```

## Składnia SQL

```sql
DLOG1(<x>)
```

## Przykłady SQL

```sql
SELECT DLOG1(2.718281828459045);

┌─────┐
│ 1.0 │
└─────┘
```
