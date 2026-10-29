---
title: ATAN (Lakehouse v2)
description: ATAN — 숫자의 아크탄젠트를 라디안 단위로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan.md
---

숫자의 아크탄젠트를 라디안 단위로 반환합니다.

## Analyze 구문

```python
func.atan(<x>)
```

## Analyze 예제

```python
func.atan(1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## SQL 구문

```sql
ATAN(<x>)
```

## SQL 예제

```sql
SELECT ATAN(1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
