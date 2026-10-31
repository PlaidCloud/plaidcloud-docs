---
title: IS_NULL（Lakehouse v1）
description: IS_NULL——检查值是否为 NULL。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-null.md
---

检查值是否为 NULL。

## Analyze 语法

```python
func.is_null(<expr>)
```

## Analyze 示例

```python
func.is_null(1)

┌─────────────────┐
│ func.is_null(1) │
├─────────────────┤
│ false           │
└─────────────────┘
```

## SQL 语法

```sql
IS_NULL(<expr>)
```

## SQL 示例

```sql
SELECT IS_NULL(1);

┌────────────┐
│ is_null(1) │
├────────────┤
│ false      │
└────────────┘
```
