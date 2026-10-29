---
title: FPOW (Lakehouse v2)
description: FPOW — alias funkcji `POW`. Zobacz [POW](../pow/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fpow.md
---

Alias funkcji `POW`. Zobacz [POW](../pow/).

## Składnia Analyze

```python
func.fpow(2, 10)
```

## Przykłady Analyze

```python
func.fpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## Składnia SQL

```sql
FPOW(<x>)
```

## Przykłady SQL

```sql
SELECT FPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
