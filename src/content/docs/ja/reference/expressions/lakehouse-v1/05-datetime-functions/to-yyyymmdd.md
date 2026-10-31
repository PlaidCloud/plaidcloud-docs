---
title: TO_YYYYMMDD (Lakehouse v1)
description: TO_YYYYMMDD — 日付または日時（timestamp/datetime）を、年月日を表す UInt32 の数値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmdd.md
---

日付または日時（timestamp/datetime）を、年月日を表す UInt32 の数値（YYYY * 10000 + MM * 100 + DD）に変換します。

## Analyze の構文

```python
func.to_yyyymmdd(<expr>)
```

## Analyze の例

```python
func.to_yyyymmdd('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ func.to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                       │
├────────────────────────────────────────────────┤
│                                       20231112 │
└────────────────────────────────────────────────┘
```

## SQL構文

```sql
TO_YYYYMMDD(<expr>)
```

## 引数

| 引数 | 説明   |
|-----------|---------------|
| `<expr>`  | 日付/日時 |

## 戻り値の型

`INT`。`YYYYMMDD` 形式で返します。

## SQLの例

```sql
SELECT
  to_yyyymmdd('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────┐
│ to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                  │
├───────────────────────────────────────────┤
│                                  20231112 │
└───────────────────────────────────────────┘
```
