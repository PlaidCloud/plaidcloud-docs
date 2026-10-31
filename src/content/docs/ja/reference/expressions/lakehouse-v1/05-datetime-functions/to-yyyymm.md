---
title: TO_YYYYMM (Lakehouse v1)
description: TO_YYYYMM — 日付または日時（timestamp/datetime）を、年月を表す UInt32 の数値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymm.md
---

日付または日時（timestamp/datetime）を、年と月を表す UInt32 の数値に変換します。

## Analyze の構文

```python
func.to_yyyymm(<expr>)
```

## Analyze の例

```python
func.to_yyyymm('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_yyyymm('2023-11-12 09:38:18.165575') │
│                   UInt32                     │
├──────────────────────────────────────────────┤
│                                       202311 │
└──────────────────────────────────────────────┘
```

## SQL構文

```sql
TO_YYYYMM(<expr>)
```

## 引数

| 引数 | 説明    |
|-----------|----------------|
| `<expr>`  | 日付/タイムスタンプ |

## 戻り値の型

`INT`。`YYYYMM` 形式で返します。

## SQLの例

```sql
SELECT
  to_yyyymm('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_yyyymm('2023-11-12 09:38:18.165575') │
│                  UInt32                 │
├─────────────────────────────────────────┤
│                                  202311 │
└─────────────────────────────────────────┘
```
