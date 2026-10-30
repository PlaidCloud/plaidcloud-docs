---
title: PERCENTILE_DISC_LC (Lakehouse v2)
description: PERCENTILE_DISC_LC — zwraca wartość percentyla przy użyciu algorytmu zoptymalizowanego pod kątem niskiej liczności.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc-lc.md
---

Zwraca wartość percentyla przy użyciu algorytmu zoptymalizowanego pod kątem niskiej liczności.

## Składnia Analyze

```python
func.percentile_disc_lc(0.5)
```

## Przykłady Analyze

```python
func.percentile_disc_lc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## Składnia SQL

```sql
PERCENTILE_DISC_LC(0.5)
```

## Przykłady SQL

```sql
SELECT PERCENTILE_DISC_LC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
