---
title: STRLEFT（Lakehouse v2）
description: STRLEFT — 文字列の左端からN文字を返します。`LEFT` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strleft.md
---

文字列の左端からN文字を返します。`LEFT` の別名です。

## Analyze 構文

```python
func.strleft(<str>, <len>)
```

## Analyze の例

```python
func.strleft('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL 構文

```sql
STRLEFT(<str>, <len>)
```

## SQL の例

```sql
SELECT STRLEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
