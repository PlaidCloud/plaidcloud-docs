---
title: TO_YYYYMMDDHH (Lakehouse v1)
description: TO_YYYYMMDDHH — 指定した日付またはタイムスタンプを「YYYYMMDDHH」形式の数値表現に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhh.md
---

指定した日付またはタイムスタンプを「YYYYMMDDHH」（年、月、日、時）形式の数値表現に変換します。

## Analyze の構文

```python
func.to_yyyymmddhh(<expr>)
```

## Analyze の例

```python
func.to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ func.to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                   UInt32                         │
├──────────────────────────────────────────────────┤
│                                       2023111209 │
└──────────────────────────────────────────────────┘
```

## SQL構文

```sql
TO_YYYYMMDDHH(<expr>)
```

## 引数

| 引数 | 説明   |
|-----------|---------------|
| `<expr>`  | 日付/日時 |

## 戻り値の型

「YYYYMMDDHH」形式の符号なし64ビット整数（UInt64）を返します。

## SQLの例

```sql
SELECT
  to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────┐
│ to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                    UInt32                   │
├─────────────────────────────────────────────┤
│                                  2023111209 │
└─────────────────────────────────────────────┘
```
