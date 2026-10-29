---
title: SQRT (Lakehouse v2)
description: SQRT — 숫자의 제곱근을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sqrt.md
---

숫자의 제곱근을 반환합니다.

## Analyze 구문

```python
func.sqrt(<x>)
```

## Analyze 예제

```python
func.sqrt(144)

┌──────┐
│ 12.0  │
└──────┘
```

## SQL 구문

```sql
SQRT(<x>)
```

## SQL 예제

```sql
SELECT SQRT(144);

┌──────┐
│ 12.0  │
└──────┘
```
