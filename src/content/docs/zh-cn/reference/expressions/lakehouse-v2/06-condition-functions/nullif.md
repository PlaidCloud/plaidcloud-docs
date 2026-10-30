---
title: NULLIF (Lakehouse v2)
description: NULLIF：如果两个表达式相等，则返回 NULL，否则返回第一个表达式。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/nullif.md
---

如果两个表达式相等，则返回 NULL，否则返回第一个表达式。

## Analyze 语法

```python
func.nullif(get_column(table, 'value'), 0)
```

## Analyze 示例

```python
func.nullif(get_column(table, 'divisor'), 0)
```

## SQL 语法

```sql
NULLIF(<value>, 0)
```

## SQL 示例

```sql
SELECT 100 / NULLIF(divisor, 0) AS safe_division FROM calculations;

┌───────────────┐
│ safe_division │
├───────────────┤
│         50.00 │
│          NULL │
│         25.00 │
└───────────────┘
```
