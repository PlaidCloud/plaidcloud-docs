---
title: SPLIT_PART（Lakehouse v2）
description: SPLIT_PART — 区切り文字で文字列を分割し、指定したインデックスの要素を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split-part.md
---

区切り文字で文字列を分割し、指定したインデックスの要素を返します。

## Analyze 構文

```python
func.split_part(<str>, <delimiter>, <index>)
```

## Analyze の例

```python
func.split_part('a-b-c', '-', 2)

┌─────┐
│ 'b'  │
└─────┘
```

## SQL 構文

```sql
SPLIT_PART(<str>, <delimiter>, <index>)
```

## SQL の例

```sql
SELECT SPLIT_PART('a-b-c', '-', 2);

┌───┐
│ b  │
└───┘
```
