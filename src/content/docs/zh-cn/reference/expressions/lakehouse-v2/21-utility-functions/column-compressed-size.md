---
title: COLUMN_COMPRESSED_SIZE (Lakehouse v2)
description: COLUMN_COMPRESSED_SIZE：返回列值压缩后的字节大小。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-compressed-size.md
---

返回列值压缩后的字节大小。

## Analyze 语法

```python
func.column_compressed_size(get_column(table, 'data'))
```

## Analyze 示例

```python
func.column_compressed_size(get_column(table, 'data'))

┌─────┐
│ 128 │
└─────┘
```

## SQL 语法

```sql
COLUMN_COMPRESSED_SIZE(<expr>)
```

## SQL 示例

```sql
SELECT COLUMN_COMPRESSED_SIZE(data) FROM records LIMIT 1;

┌─────┐
│ 128 │
└─────┘
```
