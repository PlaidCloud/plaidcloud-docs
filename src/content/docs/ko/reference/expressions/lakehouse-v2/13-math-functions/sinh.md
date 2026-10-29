---
title: SINH (Lakehouse v2)
description: SINH — 숫자의 쌍곡사인을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sinh.md
---

숫자의 쌍곡사인을 반환합니다.

## Analyze 구문

```python
func.sinh(<x>)
```

## Analyze 예제

```python
func.sinh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQL 구문

```sql
SINH(<x>)
```

## SQL 예제

```sql
SELECT SINH(0);

┌─────┐
│ 0.0  │
└─────┘
```
