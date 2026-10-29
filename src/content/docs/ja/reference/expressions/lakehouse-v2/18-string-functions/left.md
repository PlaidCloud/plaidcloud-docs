---
title: LEFT（Lakehouse v2）
description: LEFT — 文字列の左端からN文字を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/left.md
---

文字列の左端からN文字を返します。

## Analyze 構文

```python
func.left(<str>, <len>)
```

## Analyze の例

```python
func.left('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## SQL 構文

```sql
LEFT(<str>, <len>)
```

## SQL の例

```sql
SELECT LEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
