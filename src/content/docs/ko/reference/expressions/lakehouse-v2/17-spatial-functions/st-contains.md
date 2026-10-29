---
title: ST_CONTAINS (Lakehouse v2)
description: ST_CONTAINS — 한 지오메트리가 다른 지오메트리를 포함하는지 확인합니다. 포함하면 1을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-contains.md
---

한 지오메트리가 다른 지오메트리를 포함하는지 확인합니다. 포함하면 1을 반환합니다.

## Analyze 구문

```python
func.st_contains(<geometry1>, <geometry2>)
```

## Analyze 예제

```python
func.st_contains(get_column(table, 'area'), func.st_point(1, 1))

┌───┐
│ 1  │
└───┘
```

## SQL 구문

```sql
ST_CONTAINS(<geometry1>, <geometry2>)
```

## SQL 예제

```sql
SELECT ST_CONTAINS(ST_GeomFromText('POLYGON((0 0,10 0,10 10,0 10,0 0))'), ST_POINT(5, 5));

┌───┐
│ 1  │
└───┘
```
