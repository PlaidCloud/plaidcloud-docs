---
title: REGEXP_REPLACE (Lakehouse v1)
description: REGEXP_REPLACE — 文字列 expr のうち、正規表現に一致する部分を置換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-replace.md
---

文字列 `expr` のうち、パターン `pat` で指定した正規表現に一致する部分を置換文字列 `repl` に置き換え、結果の文字列を返します。`expr`、`pat`、`repl` のいずれかが NULL の場合、戻り値は NULL です。

## Analyze の構文

```python
func.regexp_replace(<expr>, <pat>, <repl[, pos[, occurrence[, match_type]]]>)
```

## Analyze の例

```python
func.regexp_replace('a b c', 'b', 'X')
┌────────────────────────────────────────┐
│ func.regexp_replace('a b c', 'b', 'X') │
├────────────────────────────────────────┤
│ a X c                                  │
└────────────────────────────────────────┘
```

## SQL構文

```sql
REGEXP_REPLACE(<expr>, <pat>, <repl[, pos[, occurrence[, match_type]]]>)
```

## 引数

| 引数  | 説明                                                                                                             |
|------------|-------------------------------------------------------------------------------------------------------------------------|
| expr       | 照合対象の文字列 expr                                                                                      |
| pat        | 正規表現                                                                                                  |
| repl       | 置換文字列                                                                                                  |
| pos        | 省略可能。expr の中で検索を開始する位置。省略した場合のデフォルトは 1 です。                              |
| occurrence | 省略可能。何番目の一致を置換するか。省略した場合のデフォルトは 0 です（「すべての一致を置換する」という意味です）。 |
| match_type | 省略可能。照合の方法を指定する文字列。意味は REGEXP_LIKE() の説明のとおりです。               |

## 戻り値の型

`VARCHAR`

## SQLの例

```sql
SELECT REGEXP_REPLACE('a b c', 'b', 'X');
┌───────────────────────────────────┐
│ REGEXP_REPLACE('a b c', 'b', 'X') │
├───────────────────────────────────┤
│ a X c                             │
└───────────────────────────────────┘

SELECT REGEXP_REPLACE('abc def ghi', '[a-z]+', 'X', 1, 3);
┌────────────────────────────────────────────────────┐
│ REGEXP_REPLACE('abc def ghi', '[a-z]+', 'X', 1, 3) │
├────────────────────────────────────────────────────┤
│ abc def X                                          │
└────────────────────────────────────────────────────┘

SELECT REGEXP_REPLACE('周 周周 周周周', '周+', 'X', 3, 2);
┌───────────────────────────────────────────────────────────┐
│ REGEXP_REPLACE('周 周周 周周周', '周+', 'X', 3, 2)        │
├───────────────────────────────────────────────────────────┤
│ 周 周周 X                                                 │
└───────────────────────────────────────────────────────────┘
```
