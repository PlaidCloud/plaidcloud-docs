---
title: TO_MONTH（Lakehouse v1）
description: TO_MONTH — 日付または日時（タイムスタンプ/datetime）を、月の番号を含む UInt8 の数値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-month.md
---

日付または日時（タイムスタンプ/datetime）を、月の番号（1～12）を表す UInt8 の数値に変換します。

## Analyze 構文

```python
func.to_month(<expr>)
```

## Analyze の例

```python
func.now(), func.to_month(func.now()), func.month(func.now())

┌─────────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_month(func.now()) │ func.month(func.now()) │
├────────────────────────────┼───────────────────────────┼────────────────────────┤
│ 2024-03-14 23:34:02.161291 │                         3 │                      3 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
TO_MONTH(<expr>)
```

## 引数

| 引数 | 説明    |
|-----------|----------------|
| `<expr>`  | 日付/タイムスタンプ |

## エイリアス

- [MONTH](../month)

## 戻り値の型

 `TINYINT`

## SQL の例

```sql
SELECT NOW(), TO_MONTH(NOW()), MONTH(NOW());

┌─────────────────────────────────────────────────────────────┐
│            now()           │ to_month(now()) │ month(now()) │
├────────────────────────────┼─────────────────┼──────────────┤
│ 2024-03-14 23:34:02.161291 │               3 │            3 │
└─────────────────────────────────────────────────────────────┘
```
