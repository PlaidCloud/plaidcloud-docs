---
title: SUBSTR（Lakehouse v2）
description: SUBSTR — 指定した位置から始まる部分文字列を返します。長さは省略できます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substr.md
---

指定した位置から始まる部分文字列を返します。長さは省略できます。

## Analyze 構文

```python
func.substr(<str>, <pos>[, <len>])
```

## Analyze の例

```python
func.substr('StarRocks', 5, 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL 構文

```sql
SUBSTR(<str>, <pos>[, <len>])
```

## SQL の例

```sql
SELECT SUBSTR('StarRocks', 5, 5);

┌───────┐
│ Rocks  │
└───────┘
```
