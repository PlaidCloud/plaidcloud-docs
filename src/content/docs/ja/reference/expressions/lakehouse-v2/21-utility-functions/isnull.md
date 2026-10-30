---
title: ISNULL（Lakehouse v2）
description: ISNULL — 値が NULL であるかどうかを判定します。NULL の場合は 1、そうでない場合は 0 を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/isnull.md
---

値が NULL であるかどうかを判定します。NULL の場合は 1、そうでない場合は 0 を返します。

## Analyze 構文

```python
func.isnull(<expr>)
```

## Analyze の例

```python
func.isnull(None)

┌───┐
│ 1  │
└───┘
```

## SQL 構文

```sql
ISNULL(<expr>)
```

## SQL の例

```sql
SELECT ISNULL(NULL);

┌───┐
│ 1  │
└───┘
```
