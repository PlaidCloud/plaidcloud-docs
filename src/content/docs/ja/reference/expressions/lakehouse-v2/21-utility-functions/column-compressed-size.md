---
title: COLUMN_COMPRESSED_SIZE（Lakehouse v2）
description: COLUMN_COMPRESSED_SIZE — 列の値の圧縮後のサイズをバイト数で返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-compressed-size.md
---

列の値の圧縮後のサイズをバイト数で返します。

## Analyze 構文

```python
func.column_compressed_size(get_column(table, 'data'))
```

## Analyze の例

```python
func.column_compressed_size(get_column(table, 'data'))

┌─────┐
│ 128 │
└─────┘
```

## SQL 構文

```sql
COLUMN_COMPRESSED_SIZE(<expr>)
```

## SQL の例

```sql
SELECT COLUMN_COMPRESSED_SIZE(data) FROM records LIMIT 1;

┌─────┐
│ 128 │
└─────┘
```
