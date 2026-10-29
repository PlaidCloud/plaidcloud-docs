---
title: DPOW (Lakehouse v2)
description: DPOW — alias funkcji `POW`. Zobacz [POW](../pow/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dpow.md
---

Alias funkcji `POW`. Zobacz [POW](../pow/).

## Składnia Analyze

```python
func.dpow(2, 10)
```

## Przykłady Analyze

```python
func.dpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## Składnia SQL

```sql
DPOW(<x>)
```

## Przykłady SQL

```sql
SELECT DPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
