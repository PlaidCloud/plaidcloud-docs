---
title: NOT REGEXP (Lakehouse v1)
description: NOT REGEXP — 文字列 expr がパターン pat で指定した正規表現に一致しない場合は 1、それ以外の場合は 0 を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-regexp.md
---

文字列 expr がパターン pat で指定した正規表現に一致しない場合は 1、それ以外の場合は 0 を返します。

## Analyze の構文

```python
not_(<column>.regexp_match(<pattern>))
```

## Analyze の例

```python

With an input table of:
┌─────────────────┐
│ my_clothes      │
├─────────────────┤
│ plaid pants     │
│ plaid hat       │
│ plaid shirt     │
│ shoes           │
└─────────────────┘

not_(my_clothes.regexp_match('p*'))
┌─────────────────────────────────────┐
│ not_(my_clothes.regexp_match('p*')) │
├─────────────────────────────────────┤
│ false                               │
│ false                               │
│ false                               │
│ true                                │
└─────────────────────────────────────┘
```

## SQL構文

```sql
<expr> NOT REGEXP <pattern>
```

## SQLの例

```sql
SELECT 'databend' NOT REGEXP 'd*';
┌──────────────────────────────┐
│ ('databend' not regexp 'd*') │
├──────────────────────────────┤
│                            0 │
└──────────────────────────────┘
```
