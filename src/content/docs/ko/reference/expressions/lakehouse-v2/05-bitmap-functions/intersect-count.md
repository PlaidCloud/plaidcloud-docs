---
title: INTERSECT_COUNT (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 INTERSECT_COUNT 비트맵 함수를 사용합니다. 차원으로 필터링한 여러 비트맵의 교집합에 있는 요소의 개수를 반환합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/intersect-count.md
---

차원으로 필터링한 여러 비트맵의 교집합에 있는 요소의 개수를 반환합니다.

## Analyze 구문

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'dim'), val1, val2)
```

## Analyze 예제

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'tag'), 1, 2)

┌─────┐
│ 150 │
└─────┘
```

## SQL 구문

```sql
INTERSECT_COUNT(<bm>, <dim>, val1, val2)
```

## SQL 예제

```sql
SELECT INTERSECT_COUNT(user_bm, tag, 1, 2) FROM segments;

┌─────┐
│ 150 │
└─────┘
```
