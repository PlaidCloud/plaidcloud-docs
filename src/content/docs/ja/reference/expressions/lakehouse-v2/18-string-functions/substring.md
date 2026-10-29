---
title: SUBSTRING（Lakehouse v2）
description: SUBSTRING — 指定した位置から始まる部分文字列を返します。`SUBSTR` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring.md
---

指定した位置から始まる部分文字列を返します。`SUBSTR` の別名です。

## Analyze 構文

```python
func.substring(<str>, <pos>[, <len>])
```

## Analyze の例

```python
func.substring('StarRocks', 1, 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL 構文

```sql
SUBSTRING(<str>, <pos>[, <len>])
```

## SQL の例

```sql
SELECT SUBSTRING('StarRocks', 1, 4);

┌──────┐
│ Star  │
└──────┘
```
