---
title: REGEXP (Lakehouse v1)
description: REGEXP – gibt true zurück, wenn die Zeichenfolge <expr> zum durch <pattern> angegebenen regulären Ausdruck passt, andernfalls false.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp.md
---

Gibt `true` zurück, wenn die Zeichenfolge `<expr>` zum durch `<pattern>` angegebenen regulären Ausdruck passt, andernfalls `false`.

## Analyze-Syntax

```python
<column>.regexp_match(<pattern>)
```

## Analyze-Beispiele

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

## SQL-Syntax

```sql
<expr> REGEXP <pattern>
```

## Aliase

- [RLIKE](../rlike)

## SQL-Beispiele

```sql
SELECT 'databend' REGEXP 'd*', 'databend' RLIKE 'd*';

┌────────────────────────────────────────────────────┐
│ ('databend' regexp 'd*') │ ('databend' rlike 'd*') │
├──────────────────────────┼─────────────────────────┤
│ true                     │ true                    │
└────────────────────────────────────────────────────┘
```
