---
title: VARIANT_GET (Lakehouse v2)
description: VARIANT_GET：从 VARIANT 对象的指定路径提取带类型的值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-get.md
---

从 VARIANT 对象的指定路径提取带类型的值。

## Analyze 语法

```python
func.variant_get(<variant>, <path>, <type>)
```

## Analyze 示例

```python
func.variant_get(get_column(table, 'data'), '$.name', 'STRING')

┌─────────┐
│ 'Alice'  │
└─────────┘
```

## SQL 语法

```sql
VARIANT_GET(<variant>, <path>, <type>)
```

## SQL 示例

```sql
SELECT VARIANT_GET(data, '$.name', 'STRING') FROM events;

┌───────┐
│ Alice  │
└───────┘
```
