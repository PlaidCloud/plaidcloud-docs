---
title: TO_QUARTER（Lakehouse v1）
description: TO_QUARTER — 指定した日付またはタイムスタンプから四半期（1、2、3、4）を取得します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-quarter.md
---

指定した日付またはタイムスタンプから四半期（1、2、3、4）を取得します。

## Analyze 構文

```python
func.to_quarter(<expr>)
```

## Analyze の例

```python
func.now(), func.to_quarter(func.now()), func.quarter(func.now())

┌─────────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_quarter(func.now()) │ func.quarter(func.now()) │
├────────────────────────────┼─────────────────────────────┼──────────────────────────┤
│ 2024-03-14 23:32:52.743133 │                           3 │                        3 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
TO_QUARTER( <date_or_time_expr> )
```

## エイリアス

- [QUARTER](../quarter)

## 戻り値の型

整数。

## SQL の例

```sql
SELECT NOW(), TO_QUARTER(NOW()), QUARTER(NOW());

┌─────────────────────────────────────────────────────────────────┐
│            now()           │ to_quarter(now()) │ quarter(now()) │
├────────────────────────────┼───────────────────┼────────────────┤
│ 2024-03-14 23:32:52.743133 │                 1 │              1 │
└─────────────────────────────────────────────────────────────────┘
```
