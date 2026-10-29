---
title: IS_NULL (Lakehouse v1)
description: IS_NULL — 값이 NULL인지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-null.md
---

값이 NULL인지 확인합니다.

## Analyze 구문

```python
func.is_null(<expr>)
```

## Analyze 예시

```python
func.is_null(1)

┌─────────────────┐
│ func.is_null(1) │
├─────────────────┤
│ false           │
└─────────────────┘
```

## SQL 구문

```sql
IS_NULL(<expr>)
```

## SQL 예시

```sql
SELECT IS_NULL(1);

┌────────────┐
│ is_null(1) │
├────────────┤
│ false      │
└────────────┘
```
