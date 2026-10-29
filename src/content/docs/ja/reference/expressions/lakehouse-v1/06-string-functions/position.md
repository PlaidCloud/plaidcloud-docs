---
title: POSITION (Lakehouse v1)
description: POSITION — POSITION(substr IN str) は LOCATE(substr,str) の同義語です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/position.md
---

POSITION(substr IN str) は LOCATE(substr,str) の同義語です。
文字列 str の中で部分文字列 substr が最初に現れる位置を返します。
substr が str に含まれない場合は 0 を返します。いずれかの引数が NULL の場合は NULL を返します。

## Analyze の構文

```python
func.position(<substr>, <str>)
```

## Analyze の例

```python
func.position('bar', 'foobarbar')
┌───────────────────────────────────┐
│ func.position('bar', 'foobarbar') │
├───────────────────────────────────┤
│                                 4 │
└───────────────────────────────────┘
```

## SQL構文

```sql
POSITION(<substr> IN <str>)
```

## 引数

| 引数 | 説明    |
|------------|----------------|
| `<substr>` | 部分文字列。 |
| `<str>`    | 文字列。    |

## 戻り値の型

`BIGINT`

## SQLの例

```sql
SELECT POSITION('bar' IN 'foobarbar')
┌────────────────────────────┐
│ POSITION('bar' IN 'foobarbar') │
├────────────────────────────┤
│                          4 │
└────────────────────────────┘

SELECT POSITION('xbar' IN 'foobar')
┌──────────────────────────┐
│ POSITION('xbar' IN 'foobar') │
├──────────────────────────┤
│                        0 │
└──────────────────────────┘
```
