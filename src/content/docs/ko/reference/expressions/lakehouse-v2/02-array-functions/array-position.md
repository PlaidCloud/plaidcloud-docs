---
title: ARRAY_POSITION (Lakehouse v2)
description: ARRAY_POSITION — 요소가 처음 나타나는 위치를 반환합니다(1부터 시작).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-position.md
---

요소가 처음 나타나는 위치를 반환합니다(1부터 시작).

## Analyze 구문

```python
func.array_position([10, 20, 30], 20)
```

## Analyze 예제

```python
func.array_position([10, 20, 30], 20)

┌───┐
│ 2 │
└───┘
```

## SQL 구문

```sql
ARRAY_POSITION([10, 20, 30], 20)
```

## SQL 예제

```sql
SELECT ARRAY_POSITION([10, 20, 30], 20);

┌───┐
│ 2 │
└───┘
```
