---
title: IS_NOT_NULL（Lakehouse v1）
description: IS_NOT_NULL——检查值是否不为 NULL。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-not-null.md
---

检查值是否不为 NULL。

## Analyze 语法

```python
func.is_not_null(<expr>)
```

## Analyze 示例

```python
func.is_not_null(1)

┌─────────────────────┐
│ func.is_not_null(1) │
├─────────────────────┤
│ true                │
└─────────────────────┘
```

## SQL 语法

```sql
IS_NOT_NULL(<expr>)
```

## SQL 示例

```sql
SELECT IS_NOT_NULL(1);

┌────────────────┐
│ is_not_null(1) │
├────────────────┤
│ true           │
└────────────────┘
```
