---
title: TO_YEAR (Lakehouse v1)
description: TO_YEAR — 日付または日時（timestamp/datetime）を、西暦の年を表す UInt16 の数値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-year.md
---

日付または日時（timestamp/datetime）を、西暦の年を表す UInt16 の数値に変換します。

## Analyze の構文

```python
func.to_year(<expr>)
```

## Analyze の例

```python
func.now(), func.to_year(func.now()), func.year(func.now())

┌───────────────────────────────────────────────────────────────────────────────┐
│       func.now()           │ func.to_year(func.now()) │ func.year(func.now()) │
├────────────────────────────┼──────────────────────────┼───────────────────────┤
│ 2024-03-14 23:37:03.895166 │                     2024 │                  2024 │
└───────────────────────────────────────────────────────────────────────────────┘
```

## SQL構文

```sql
TO_YEAR(<expr>)
```

## 引数

| 引数 | 説明    |
|-----------|----------------|
| `<expr>`  | 日付/タイムスタンプ |

## エイリアス

- [YEAR](../year)

## 戻り値の型

 `SMALLINT`

## SQLの例

```sql
SELECT NOW(), TO_YEAR(NOW()), YEAR(NOW());

┌───────────────────────────────────────────────────────────┐
│            now()           │ to_year(now()) │ year(now()) │
├────────────────────────────┼────────────────┼─────────────┤
│ 2024-03-14 23:37:03.895166 │           2024 │        2024 │
└───────────────────────────────────────────────────────────┘
```
