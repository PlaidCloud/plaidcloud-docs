---
title: ERROR_OR (Lakehouse v1)
description: ERROR_OR — 입력된 식 중 오류가 아닌 첫 번째 식을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/error-or.md
---

입력된 식 중 오류가 아닌 첫 번째 식을 반환합니다. 모든 식에서 오류가 발생하면 NULL을 반환합니다.

## Analyze 구문

```python
func.error_or(expr1, expr2, ...)
```

## Analyze 예시

```python
# Returns the valid date if no errors occur
# Returns the current date if the conversion results in an error
func.now(), func.error_or(func.to_date('2024-12-25'), func.now())

┌──────────────────────────────────────────────────────────────────────────────────────────┐
│            func.now()           │ func.error_or(func.to_date('2024-12-25'), func.now())  │
├─────────────────────────────────┼────────────────────────────────────────────────────────┤
│ 2024-03-18 01:22:39.460320      │ 2024-12-25                                             │
└──────────────────────────────────────────────────────────────────────────────────────────┘

# Returns NULL because the conversion results in an error
func.error_or(func.to_date('2024-1234'))

┌────────────────────────────────────────────┐
│ func.error_or(func.to_date('2024-1234'))   │
├────────────────────────────────────────────┤
│ NULL                                       │
└────────────────────────────────────────────┘
```

## SQL 구문

```sql
ERROR_OR(expr1, expr2, ...)
```

## SQL 예시

```sql
-- Returns the valid date if no errors occur
-- Returns the current date if the conversion results in an error
SELECT NOW(), ERROR_OR('2024-12-25'::DATE, NOW()::DATE);

┌────────────────────────────────────────────────────────────────────────┐
│            now()           │ error_or('2024-12-25'::date, now()::date) │
├────────────────────────────┼───────────────────────────────────────────┤
│ 2024-03-18 01:22:39.460320 │ 2024-12-25                                │
└────────────────────────────────────────────────────────────────────────┘

-- Returns NULL because the conversion results in an error
SELECT ERROR_OR('2024-1234'::DATE);

┌─────────────────────────────┐
│ error_or('2024-1234'::date) │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘
```
