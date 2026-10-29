---
title: PERCENTILE_DISC_LC (Lakehouse v2)
description: PERCENTILE_DISC_LC — 낮은 카디널리티에 최적화된 알고리즘을 사용하여 백분위수 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc-lc.md
---

낮은 카디널리티에 최적화된 알고리즘을 사용하여 백분위수 값을 반환합니다.

## Analyze 구문

```python
func.percentile_disc_lc(0.5)
```

## Analyze 예제

```python
func.percentile_disc_lc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## SQL 구문

```sql
PERCENTILE_DISC_LC(0.5)
```

## SQL 예제

```sql
SELECT PERCENTILE_DISC_LC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
