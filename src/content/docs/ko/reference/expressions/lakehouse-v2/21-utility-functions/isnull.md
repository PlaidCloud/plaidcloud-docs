---
title: ISNULL (Lakehouse v2)
description: ISNULL — 값이 NULL인지 확인합니다. NULL이면 1을, 그렇지 않으면 0을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnull.md
---

값이 NULL인지 확인합니다. NULL이면 1을, 그렇지 않으면 0을 반환합니다.

## Analyze 구문

```python
func.isnull(<expr>)
```

## Analyze 예제

```python
func.isnull(None)

┌───┐
│ 1  │
└───┘
```

## SQL 구문

```sql
ISNULL(<expr>)
```

## SQL 예제

```sql
SELECT ISNULL(NULL);

┌───┐
│ 1  │
└───┘
```
