---
title: TANH (Lakehouse v2)
description: TANH — 숫자의 쌍곡탄젠트를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tanh.md
---

숫자의 쌍곡탄젠트를 반환합니다.

## Analyze 구문

```python
func.tanh(<x>)
```

## Analyze 예제

```python
func.tanh(0)

┌─────┐
│ 0.0  │
└─────┘
```

## SQL 구문

```sql
TANH(<x>)
```

## SQL 예제

```sql
SELECT TANH(0);

┌─────┐
│ 0.0  │
└─────┘
```
