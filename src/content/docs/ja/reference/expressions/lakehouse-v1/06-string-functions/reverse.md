---
title: REVERSE (Lakehouse v1)
description: REVERSE — 文字列 str の文字の順序を逆にした文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/reverse.md
---

文字列 str の文字の順序を逆にした文字列を返します。

## Analyze の構文

```python
func.reverse(<str>)
```

## Analyze の例

```python
func.reverse('abc')
┌──────────────────────┐
│ func..reverse('abc') │
├──────────────────────┤
│ cba                  │
└──────────────────────┘
```

## SQL構文

```sql
REVERSE(<str>)
```

## 引数

| 引数 | 説明       |
|-----------|-------------------|
| `<str>`   | 文字列値。 |

## 戻り値の型

`VARCHAR`

## SQLの例

```sql
SELECT REVERSE('abc');
┌────────────────┐
│ REVERSE('abc') │
├────────────────┤
│ cba            │
└────────────────┘
```
