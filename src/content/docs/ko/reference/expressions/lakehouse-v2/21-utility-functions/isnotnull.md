---
title: ISNOTNULL (Lakehouse v2)
description: ISNOTNULL — 값이 NULL이 아닌지 확인합니다. NULL이 아니면 1을, 그렇지 않으면 0을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnotnull.md
---

값이 NULL이 아닌지 확인합니다. NULL이 아니면 1을, 그렇지 않으면 0을 반환합니다.

## Analyze 구문

```python
func.isnotnull(<expr>)
```

## Analyze 예제

```python
func.isnotnull(1)

┌───┐
│ 1  │
└───┘
```

## SQL 구문

```sql
ISNOTNULL(<expr>)
```

## SQL 예제

```sql
SELECT ISNOTNULL(1);

┌───┐
│ 1  │
└───┘
```
