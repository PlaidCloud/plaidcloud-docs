---
title: LOG2 (Lakehouse v2)
description: LOG2 — 숫자의 밑 2 로그를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log2.md
---

숫자의 밑 2 로그를 반환합니다.

## Analyze 구문

```python
func.log2(<x>)
```

## Analyze 예제

```python
func.log2(8)

┌─────┐
│ 3.0  │
└─────┘
```

## SQL 구문

```sql
LOG2(<x>)
```

## SQL 예제

```sql
SELECT LOG2(8);

┌─────┐
│ 3.0  │
└─────┘
```
