---
title: NEGATIVE (Lakehouse v2)
description: NEGATIVE — 숫자의 부호를 반전한 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/negative.md
---

숫자의 부호를 반전한 값을 반환합니다.

## Analyze 구문

```python
func.negative(<x>)
```

## Analyze 예제

```python
func.negative(5)

┌────┐
│ -5  │
└────┘
```

## SQL 구문

```sql
NEGATIVE(<x>)
```

## SQL 예제

```sql
SELECT NEGATIVE(5);

┌────┐
│ -5  │
└────┘
```
