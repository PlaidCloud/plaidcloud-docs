---
title: SUM_MAP (Lakehouse v2)
description: SUM_MAP — 맵 열의 키별로 값을 그룹화하여 합산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum-map.md
---

맵 열의 키별로 값을 그룹화하여 합산합니다.

## Analyze 구문

```python
func.sum_map(get_column(table, 'key_col'), get_column(table, 'val_col'))
```

## Analyze 예제

```python
func.sum_map(get_column(table, 'keys'), get_column(table, 'values'))

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## SQL 구문

```sql
SUM_MAP(<key_col>, <val_col>)
```

## SQL 예제

```sql
SELECT SUM_MAP(keys, values) FROM metrics;

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
