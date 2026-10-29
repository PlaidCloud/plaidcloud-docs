---
title: ERROR_OR（Lakehouse v1）
description: ERROR_OR——返回输入中第一个不是错误的表达式。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/error-or.md
---

返回输入中第一个不是错误的表达式。如果所有表达式都产生错误，则返回 NULL。

## Analyze 语法

```python
func.error_or(expr1, expr2, ...)
```

## Analyze 示例

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

## SQL 语法

```sql
ERROR_OR(expr1, expr2, ...)
```

## SQL 示例

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
