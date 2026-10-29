---
title: DEGREES (Lakehouse v2)
description: DEGREES — 라디안을 도로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/degrees.md
---

라디안을 도로 변환합니다.

## Analyze 구문

```python
func.degrees(<x>)
```

## Analyze 예제

```python
func.degrees(3.141592653589793)

┌───────┐
│ 180.0  │
└───────┘
```

## SQL 구문

```sql
DEGREES(<x>)
```

## SQL 예제

```sql
SELECT DEGREES(PI());

┌───────┐
│ 180.0  │
└───────┘
```
