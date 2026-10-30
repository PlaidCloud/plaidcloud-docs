---
title: REGEXP_SUBSTR (Lakehouse v1)
description: REGEXP_SUBSTR — 文字列 expr のうち、正規表現に一致する部分文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-substr.md
---

文字列 `expr` のうち、パターン `pat` で指定した正規表現に一致する部分文字列を返します。一致しない場合は NULL を返します。expr または pat が NULL の場合、戻り値は NULL です。

## Analyze の構文

```python
func.regexp_substr(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## Analyze の例

```python
func.regexp_substr('abc def ghi', '[a-z]+')
┌─────────────────────────────────────────────┐
│ func.regexp_substr('abc def ghi', '[a-z]+') │
├─────────────────────────────────────────────┤
│ abc                                         │
└─────────────────────────────────────────────┘
```

## SQL構文

```sql
REGEXP_SUBSTR(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## 引数

| 引数  | 説明                                                                                               |
|------------|-----------------------------------------------------------------------------------------------------------|
| expr       | 照合対象の文字列 expr                                                                        |
| pat        | 正規表現                                                                                    |
| pos        | 省略可能。expr の中で検索を開始する位置。省略した場合のデフォルトは 1 です。                |
| occurrence | 省略可能。何番目の一致を検索するか。省略した場合のデフォルトは 1 です。                        |
| match_type | 省略可能。照合の方法を指定する文字列。意味は REGEXP_LIKE() の説明のとおりです。 |

## 戻り値の型

`VARCHAR`

## SQLの例

```sql
SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+');
┌────────────────────────────────────────┐
│ REGEXP_SUBSTR('abc def ghi', '[a-z]+') │
├────────────────────────────────────────┤
│ abc                                    │
└────────────────────────────────────────┘

SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+', 1, 3);
┌──────────────────────────────────────────────┐
│ REGEXP_SUBSTR('abc def ghi', '[a-z]+', 1, 3) │
├──────────────────────────────────────────────┤
│ ghi                                          │
└──────────────────────────────────────────────┘

SELECT REGEXP_SUBSTR('周 周周 周周周 周周周周', '周+', 2, 3);
┌──────────────────────────────────────────────────────────────────┐
│ REGEXP_SUBSTR('周 周周 周周周 周周周周', '周+', 2, 3)            │
├──────────────────────────────────────────────────────────────────┤
│ 周周周周                                                         │
└──────────────────────────────────────────────────────────────────┘

```
