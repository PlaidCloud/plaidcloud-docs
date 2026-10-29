---
title: LEFT (Lakehouse v1)
description: LEFT — 文字列 str の左端から len 文字分を返します。いずれかの引数が NULL の場合は NULL を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/left.md
---

文字列 str の左端から len 文字分を返します。いずれかの引数が NULL の場合は NULL を返します。

## Analyze の構文

```python
func.left(<str>, <len>)
```

## Analyze の例

```python
func.left('foobarbar', 5)
┌───────────────────────────┐
│ func.left('foobarbar', 5) │
├───────────────────────────┤
│ fooba                     │
└───────────────────────────┘
```

## SQL構文

```sql
LEFT(<str>, <len>);
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
SELECT LEFT('foobarbar', 5);
┌──────────────────────┐
│ LEFT('foobarbar', 5) │
├──────────────────────┤
│ fooba                │
└──────────────────────┘
```
