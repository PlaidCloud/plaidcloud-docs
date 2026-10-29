---
title: REGEXP (Lakehouse v1)
description: REGEXP — 文字列 <expr> が <pattern> で指定した正規表現に一致する場合は true、それ以外の場合は false を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp.md
---

文字列 `<expr>` が `<pattern>` で指定した正規表現に一致する場合は `true`、それ以外の場合は `false` を返します。

## Analyze の構文

```python
<column>.regexp_match(<pattern>)
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

my_clothes.regexp_match('p*')
┌───────────────────────────────┐
│ my_clothes.regexp_match('p*') │
├───────────────────────────────┤
│ true                          │
│ true                          │
│ true                          │
│ false                         │
└───────────────────────────────┘
```

## SQL構文

```sql
<expr> REGEXP <pattern>
```

## エイリアス

- [RLIKE](../rlike)

## SQLの例

```sql
SELECT 'databend' REGEXP 'd*', 'databend' RLIKE 'd*';

┌────────────────────────────────────────────────────┐
│ ('databend' regexp 'd*') │ ('databend' rlike 'd*') │
├──────────────────────────┼─────────────────────────┤
│ true                     │ true                    │
└────────────────────────────────────────────────────┘
```
