---
title: INSERT (Lakehouse v1)
description: INSERT — 文字列 str のうち、位置 pos から len 文字分の部分文字列を newstr に置き換えた文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/insert.md
---

文字列 str のうち、位置 pos から始まる len 文字分の部分文字列を、文字列 newstr に置き換えた結果を返します。pos が文字列の長さの範囲外の場合は、元の文字列を返します。len が位置 pos 以降の残りの文字列の長さを超える場合は、位置 pos 以降の残りすべてを置き換えます。いずれかの引数が NULL の場合は NULL を返します。

## Analyze の構文

```python
func.insert(<str>, <pos>, <len>, <newstr>)
```

## Analyze の例

```python
func.insert('Quadratic', 3, 4, 'What')
┌────────────────────────────────────────┐
│ func.insert('Quadratic', 3, 4, 'What') │
├────────────────────────────────────────┤
│ QuWhattic                              │
└────────────────────────────────────────┘
```

## SQL構文

```sql
INSERT(<str>, <pos>, <len>, <newstr>)
```

## 引数

| 引数  | 説明     |
|------------|-----------------|
| `<str>`    | 文字列。     |
| `<pos>`    | 位置。   |
| `<len>`    | 長さ。     |
| `<newstr>` | 新しい文字列。 |

## 戻り値の型

`VARCHAR`

## SQLの例

```sql
SELECT INSERT('Quadratic', 3, 4, 'What');
┌───────────────────────────────────┐
│ INSERT('Quadratic', 3, 4, 'What') │
├───────────────────────────────────┤
│ QuWhattic                         │
└───────────────────────────────────┘

SELECT INSERT('Quadratic', -1, 4, 'What');
┌───────────────────────────────────────┐
│ INSERT('Quadratic', (- 1), 4, 'What') │
├───────────────────────────────────────┤
│ Quadratic                             │
└───────────────────────────────────────┘

SELECT INSERT('Quadratic', 3, 100, 'What');
┌─────────────────────────────────────┐
│ INSERT('Quadratic', 3, 100, 'What') │
├─────────────────────────────────────┤
│ QuWhat                              │
└─────────────────────────────────────┘

┌────────────────────────────────────────────┬────────┐
│ INSERT('123456789', number, number, 'aaa') │ number │
├────────────────────────────────────────────┼────────┤
│ 123456789                                  │      0 │
│ aaa23456789                                │      1 │
│ 1aaa456789                                 │      2 │
│ 12aaa6789                                  │      3 │
│ 123aaa89                                   │      4 │
│ 1234aaa                                    │      5 │
│ 12345aaa                                   │      6 │
│ 123456aaa                                  │      7 │
│ 1234567aaa                                 │      8 │
│ 12345678aaa                                │      9 │
│ 123456789                                  │     10 │
│ 123456789                                  │     11 │
│ 123456789                                  │     12 │
└────────────────────────────────────────────┴────────┘
```
