---
title: DLOG10 (Lakehouse v2)
description: DLOG10 — alias funkcji `LOG10`. Zobacz [LOG10](../log10/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog10.md
---

Alias funkcji `LOG10`. Zobacz [LOG10](../log10/).

## Składnia Analyze

```python
func.dlog10(1000)
```

## Przykłady Analyze

```python
func.dlog10(1000)

┌─────┐
│ 3.0 │
└─────┘
```

## Składnia SQL

```sql
DLOG10(<x>)
```

## Przykłady SQL

```sql
SELECT DLOG10(1000);

┌─────┐
│ 3.0 │
└─────┘
```
