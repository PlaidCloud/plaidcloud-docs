---
title: BIT_LENGTH (Lakehouse v1)
description: BIT_LENGTH — 文字列の長さをビット数で返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bit-length.md
---

文字列の長さをビット数で返します。

## Analyze の構文

```python
func.bit_length(<expr>)
```

## Analyze の例

```python
func.bit_length('Word')
┌─────────────────────────┐
│ func.bit_length('Word') │
├─────────────────────────┤
│                      32 │
└─────────────────────────┘
```

## SQL構文

```sql
BIT_LENGTH(<expr>)
```

## 引数

| 引数 | 説明 |
|-----------| ----------- |
| `<expr>`  | 文字列。 |

## 戻り値の型

`BIGINT`

## SQLの例

```sql
SELECT BIT_LENGTH('Word');
┌────────────────────────────┐
│ SELECT BIT_LENGTH('Word'); │
├────────────────────────────┤
│ 32                         │
└────────────────────────────┘
```
