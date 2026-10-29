---
title: REGEXP_INSTR (Lakehouse v1)
description: REGEXP_INSTR — 文字列 expr のうち、パターン pat で指定した正規表現に一致する部分文字列の開始位置を返します。一致しない場合は 0 を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-instr.md
---

文字列 `expr` のうち、パターン `pat` で指定した正規表現に一致する部分文字列の開始位置を返します。一致しない場合は `0` を返します。`expr` または `pat` が NULL の場合、戻り値は NULL です。文字位置は `1` から始まります。

## Analyze の構文

```python
func.regexp_instr(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## Analyze の例

```python
func.regexp_instr('dog cat dog', 'dog')
┌─────────────────────────────────────────┐
│ func.regexp_instr('dog cat dog', 'dog') │
├─────────────────────────────────────────┤
│                                       1 │
└─────────────────────────────────────────┘
```

## SQL構文

```sql
REGEXP_INSTR(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## 引数

| 引数     | 説明                                                                                                                                                                                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expr          | 照合対象の文字列 expr                                                                                                                                                                                                                                     |
| pat           | 正規表現                                                                                                                                                                                                                                                 |
| pos           | 省略可能。expr の中で検索を開始する位置。省略した場合のデフォルトは 1 です。                                                                                                                                                                             |
| occurrence    | 省略可能。何番目の一致を検索するか。省略した場合のデフォルトは 1 です。                                                                                                                                                                                     |
| return_option | 省略可能。返す位置の種類。この値が 0 の場合、REGEXP_INSTR() は一致した部分文字列の先頭文字の位置を返します。この値が 1 の場合は、一致した部分文字列の直後の位置を返します。省略した場合のデフォルトは 0 です。 |
| match_type    | 省略可能。照合の方法を指定する文字列。意味は REGEXP_LIKE() の説明のとおりです。                                                                                                                                                              |

## 戻り値の型

数値データ型の値。

## SQLの例

```sql
SELECT REGEXP_INSTR('dog cat dog', 'dog');
┌────────────────────────────────────┐
│ REGEXP_INSTR('dog cat dog', 'dog') │
├────────────────────────────────────┤
│                                  1 │
└────────────────────────────────────┘

SELECT REGEXP_INSTR('dog cat dog', 'dog', 2);
┌───────────────────────────────────────┐
│ REGEXP_INSTR('dog cat dog', 'dog', 2) │
├───────────────────────────────────────┤
│                                     9 │
└───────────────────────────────────────┘

SELECT REGEXP_INSTR('aa aaa aaaa', 'a{2}');
┌─────────────────────────────────────┐
│ REGEXP_INSTR('aa aaa aaaa', 'a{2}') │
├─────────────────────────────────────┤
│                                   1 │
└─────────────────────────────────────┘

SELECT REGEXP_INSTR('aa aaa aaaa', 'a{4}');
┌─────────────────────────────────────┐
│ REGEXP_INSTR('aa aaa aaaa', 'a{4}') │
├─────────────────────────────────────┤
│                                   8 │
└─────────────────────────────────────┘
```
