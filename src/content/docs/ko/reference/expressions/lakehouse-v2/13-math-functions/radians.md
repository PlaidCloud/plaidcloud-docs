---
title: RADIANS (Lakehouse v2)
description: RADIANS — 도를 라디안으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/radians.md
---

도를 라디안으로 변환합니다.

## Analyze 구문

```python
func.radians(<x>)
```

## Analyze 예제

```python
func.radians(180)

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```

## SQL 구문

```sql
RADIANS(<x>)
```

## SQL 예제

```sql
SELECT RADIANS(180);

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```
