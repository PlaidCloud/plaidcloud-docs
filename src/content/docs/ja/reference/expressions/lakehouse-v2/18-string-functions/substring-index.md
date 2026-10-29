---
title: SUBSTRING_INDEX（Lakehouse v2）
description: "PlaidCloud Lakehouse で SUBSTRING_INDEX 文字列関数を使用します。区切り文字が指定した回数現れる位置より前または後ろの部分文字列を返します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring-index.md
---

区切り文字が指定した回数現れる位置より前または後ろの部分文字列を返します。

## Analyze 構文

```python
func.substring_index(<str>, <delim>, <count>)
```

## Analyze の例

```python
func.substring_index('www.example.com', '.', 2)

┌───────────────┐
│ 'www.example'  │
└───────────────┘
```

## SQL 構文

```sql
SUBSTRING_INDEX(<str>, <delim>, <count>)
```

## SQL の例

```sql
SELECT SUBSTRING_INDEX('www.example.com', '.', 2);

┌─────────────┐
│ www.example  │
└─────────────┘
```
