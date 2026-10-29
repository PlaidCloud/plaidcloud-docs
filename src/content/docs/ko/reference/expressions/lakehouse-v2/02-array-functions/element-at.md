---
title: "ELEMENT_AT (Array, Lakehouse v2)"
description: ELEMENT_AT — 배열에서 지정한 위치의 요소를 반환합니다(1부터 시작).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/element-at.md
---

배열에서 지정한 위치의 요소를 반환합니다(1부터 시작).

## Analyze 구문

```python
func.element_at([10, 20, 30], 2)
```

## Analyze 예제

```python
func.element_at([10, 20, 30], 2)

┌────┐
│ 20 │
└────┘
```

## SQL 구문

```sql
ELEMENT_AT([10, 20, 30], 2)
```

## SQL 예제

```sql
SELECT ELEMENT_AT([10, 20, 30], 2);

┌────┐
│ 20 │
└────┘
```
