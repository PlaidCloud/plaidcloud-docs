---
title: STRRIGHT（Lakehouse v2）
description: STRRIGHT — 文字列の右端からN文字を返します。`RIGHT` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strright.md
---

文字列の右端からN文字を返します。`RIGHT` の別名です。

## Analyze 構文

```python
func.strright(<str>, <len>)
```

## Analyze の例

```python
func.strright('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL 構文

```sql
STRRIGHT(<str>, <len>)
```

## SQL の例

```sql
SELECT STRRIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
