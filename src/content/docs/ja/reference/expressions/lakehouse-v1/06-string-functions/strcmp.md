---
title: STRCMP (Lakehouse v1)
description: STRCMP — 文字列が同じ場合は 0、1番目の引数が2番目より小さい場合は -1、それ以外の場合は 1 を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/strcmp.md
---

文字列が同じ場合は 0、1番目の引数が2番目より小さい場合は -1、それ以外の場合は 1 を返します。

## Analyze の構文

```python
func.strcmp(<expr1> ,<expr2>)
```

## Analyze の例

```python
func.strcmp('text', 'text2')
┌──────────────────────────────┐
│ func.strcmp('text', 'text2') │
├──────────────────────────────┤
│                           -1 │
└──────────────────────────────┘

func.strcmp('text2', 'text')
┌──────────────────────────────┐
│ func.strcmp('text2', 'text') │
├──────────────────────────────┤
│                            1 │
└──────────────────────────────┘

func.strcmp('text', 'text')
┌──────────────────────────────┐
│ func.strcmp('text', 'text')  │
├──────────────────────────────┤
│                            0 │
└──────────────────────────────┘
```

## SQL構文

```sql
STRCMP(<expr1> ,<expr2>)
```

## 引数

| 引数 | 説明 |
|-----------|-------------|
| `<expr1>` | 文字列。 |
| `<expr2>` | 文字列。 |

## 戻り値の型

`BIGINT`

## SQLの例

```sql
SELECT STRCMP('text', 'text2');
┌─────────────────────────┐
│ STRCMP('text', 'text2') │
├─────────────────────────┤
│                      -1 │
└─────────────────────────┘

SELECT STRCMP('text2', 'text');
┌─────────────────────────┐
│ STRCMP('text2', 'text') │
├─────────────────────────┤
│                       1 │
└─────────────────────────┘

SELECT STRCMP('text', 'text');
┌────────────────────────┐
│ STRCMP('text', 'text') │
├────────────────────────┤
│                      0 │
└────────────────────────┘
```
