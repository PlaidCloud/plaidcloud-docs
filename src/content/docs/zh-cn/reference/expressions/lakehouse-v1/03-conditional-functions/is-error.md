---
title: IS_ERROR（Lakehouse v1）
description: IS_ERROR——返回布尔值，指示表达式是否为错误值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-error.md
---

返回布尔值，指示表达式是否为错误值。

另请参阅：[IS_NOT_ERROR](../is-not-error)

## Analyze 语法

```python
func.is_error( <expr> )
```

## Analyze 示例

```python
# Indicates division by zero, hence an error
func.is_error((1 / 0)), func.is_not_error((1 / 0))

┌─────────────────────────────────────────────────────┐
│ func.is_error((1 / 0)) │ func.is_not_error((1 / 0)) │
├────────────────────────┼────────────────────────────┤
│ true                   │ false                      │
└─────────────────────────────────────────────────────┘

# The conversion to DATE is successful, hence not an error
func.is_error(func.to_date('2024-03-17')), func.is_not_error(func.to_date('2024-03-17'))

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_error(func.to_date('2024-03-17')) │ func.is_not_error(func.to_date('2024-03-17')) │
├───────────────────────────────────────────┼───────────────────────────────────────────────┤
│ false                                     │ true                                          │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
IS_ERROR( <expr> )
```

## 返回类型

如果表达式是错误，返回 `true`，否则返回 `false`。

## SQL 示例

```sql
-- Indicates division by zero, hence an error
SELECT IS_ERROR(1/0), IS_NOT_ERROR(1/0);

┌───────────────────────────────────────────┐
│ is_error((1 / 0)) │ is_not_error((1 / 0)) │
├───────────────────┼───────────────────────┤
│ true              │ false                 │
└───────────────────────────────────────────┘

-- The conversion to DATE is successful, hence not an error
SELECT IS_ERROR('2024-03-17'::DATE), IS_NOT_ERROR('2024-03-17'::DATE);

┌─────────────────────────────────────────────────────────────────┐
│ is_error('2024-03-17'::date) │ is_not_error('2024-03-17'::date) │
├──────────────────────────────┼──────────────────────────────────┤
│ false                        │ true                             │
└─────────────────────────────────────────────────────────────────┘
```
