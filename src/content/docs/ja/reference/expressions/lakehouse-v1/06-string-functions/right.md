---
title: RIGHT (Lakehouse v1)
description: RIGHT — 文字列 str の右端から len 文字分を返します。いずれかの引数が NULL の場合は NULL を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/right.md
---

文字列 str の右端から len 文字分を返します。いずれかの引数が NULL の場合は NULL を返します。

## Analyze の構文

```python
func.right(<str>, <len>)
```

## Analyze の例

```python
func.right('foobarbar', 4)
┌────────────────────────────┐
│ func.right('foobarbar', 4) │
├────────────────────────────┤
│ rbar                       │
└────────────────────────────┘
```

## SQL構文

```sql
RIGHT(<str>, <len>);
```

## 引数

| 引数 | 説明                                              |
|-----------|----------------------------------------------------------|
| `<str>`   | 文字を抽出する元の文字列 |
| `<len>`   | 文字数                                  |

## 戻り値の型

`VARCHAR`

## SQLの例

```sql
SELECT RIGHT('foobarbar', 4);
┌───────────────────────┐
│ RIGHT('foobarbar', 4) │
├───────────────────────┤
│ rbar                  │
└───────────────────────┘
```
