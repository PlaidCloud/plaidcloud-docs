---
title: RIGHT（Lakehouse v2）
description: RIGHT — 文字列の右端からN文字を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/right.md
---

文字列の右端からN文字を返します。

## Analyze 構文

```python
func.right(<str>, <len>)
```

## Analyze の例

```python
func.right('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL 構文

```sql
RIGHT(<str>, <len>)
```

## SQL の例

```sql
SELECT RIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
