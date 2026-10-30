---
title: ENCODE_SORT_KEY（Lakehouse v2）
description: "PlaidCloud Lakehouse で ENCODE_SORT_KEY ユーティリティ関数を使用します。ソート順を保持するバイナリのソートキーに値をエンコードします。複合ソートキーに便利です。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/encode-sort-key.md
---

ソート順を保持するバイナリのソートキーに値をエンコードします。複合ソートキーに便利です。

## Analyze 構文

```python
func.encode_sort_key(get_column(table, 'col1'), get_column(table, 'col2'))
```

## Analyze の例

```python
func.encode_sort_key(get_column(table, 'name'), get_column(table, 'age'))

┌───────────────────┐
│ (binary sort key) │
└───────────────────┘
```

## SQL 構文

```sql
ENCODE_SORT_KEY(<expr1>[, <expr2>, ...])
```

## SQL の例

```sql
SELECT HEX(ENCODE_SORT_KEY('Alice', 30));

┌────────────────────────┐
│ (hex-encoded sort key) │
└────────────────────────┘
```
