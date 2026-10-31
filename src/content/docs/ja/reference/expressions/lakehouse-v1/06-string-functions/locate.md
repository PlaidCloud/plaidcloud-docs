---
title: LOCATE (Lakehouse v1)
description: LOCATE — 1つ目の構文は、文字列 str の中で部分文字列 substr が最初に現れる位置を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/locate.md
---

1つ目の構文は、文字列 str の中で部分文字列 substr が最初に現れる位置を返します。
2つ目の構文は、位置 pos から検索を開始し、文字列 str の中で部分文字列 substr が最初に現れる位置を返します。
substr が str に含まれない場合は 0 を返します。いずれかの引数が NULL の場合は NULL を返します。

## Analyze の構文

```python
func.locate(<substr>, <str>, <pos>)
```

## Analyze の例

```python
func.locate('bar', 'foobarbar')
┌────────────────────────────────────┐
│ func.locate('bar', 'foobarbar') │
├────────────────────────────────────┤
│                                  5 │
└────────────────────────────────────┘
```

```python
func.locate('bar', 'foobarbar', 5)
┌────────────────────────────────────┐
│ func.locate('bar', 'foobarbar', 5) │
├────────────────────────────────────┤
│                                  7 │
└────────────────────────────────────┘
```

## SQL構文

```sql
LOCATE(<substr>, <str>)
LOCATE(<substr>, <str>, <pos>)
```

## 引数

| 引数 | 説明    |
|------------|----------------|
| `<substr>` | 部分文字列。 |
| `<str>`    | 文字列。    |
| `<pos>`    | 位置。  |

## 戻り値の型

`BIGINT`

## SQLの例

```sql
SELECT LOCATE('bar', 'foobarbar')
┌────────────────────────────┐
│ LOCATE('bar', 'foobarbar') │
├────────────────────────────┤
│                          4 │
└────────────────────────────┘

SELECT LOCATE('xbar', 'foobar')
┌──────────────────────────┐
│ LOCATE('xbar', 'foobar') │
├──────────────────────────┤
│                        0 │
└──────────────────────────┘

SELECT LOCATE('bar', 'foobarbar', 5)
┌───────────────────────────────┐
│ LOCATE('bar', 'foobarbar', 5) │
├───────────────────────────────┤
│                             7 │
└───────────────────────────────┘
```
