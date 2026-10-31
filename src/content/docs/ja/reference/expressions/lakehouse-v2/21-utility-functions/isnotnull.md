---
title: ISNOTNULL（Lakehouse v2）
description: ISNOTNULL — 値が NULL でないかどうかを判定します。NULL でない場合は 1、そうでない場合は 0 を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnotnull.md
---

値が NULL でないかどうかを判定します。NULL でない場合は 1、そうでない場合は 0 を返します。

## Analyze 構文

```python
func.isnotnull(<expr>)
```

## Analyze の例

```python
func.isnotnull(1)

┌───┐
│ 1  │
└───┘
```

## SQL 構文

```sql
ISNOTNULL(<expr>)
```

## SQL の例

```sql
SELECT ISNOTNULL(1);

┌───┐
│ 1  │
└───┘
```
