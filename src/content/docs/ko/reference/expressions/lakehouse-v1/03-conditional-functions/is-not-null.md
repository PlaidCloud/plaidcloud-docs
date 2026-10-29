---
title: IS_NOT_NULL (Lakehouse v1)
description: IS_NOT_NULL — 값이 NULL이 아닌지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-not-null.md
---

값이 NULL이 아닌지 확인합니다.

## Analyze 구문

```python
func.is_not_null(<expr>)
```

## Analyze 예시

```python
func.is_not_null(1)

┌─────────────────────┐
│ func.is_not_null(1) │
├─────────────────────┤
│ true                │
└─────────────────────┘
```

## SQL 구문

```sql
IS_NOT_NULL(<expr>)
```

## SQL 예시

```sql
SELECT IS_NOT_NULL(1);

┌────────────────┐
│ is_not_null(1) │
├────────────────┤
│ true           │
└────────────────┘
```
