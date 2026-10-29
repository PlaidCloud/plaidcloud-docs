---
title: REGEXP (Lakehouse v1)
description: REGEXP — zwraca true, jeśli ciąg znaków <expr> pasuje do wyrażenia regularnego określonego przez <pattern>, w przeciwnym razie false.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp.md
---

Zwraca `true`, jeśli ciąg znaków `<expr>` pasuje do wyrażenia regularnego określonego przez `<pattern>`, w przeciwnym razie `false`.

## Składnia Analyze

```python
<column>.regexp_match(<pattern>)
```

## Przykłady Analyze

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

## Składnia SQL

```sql
<expr> REGEXP <pattern>
```

## Aliasy

- [RLIKE](../rlike)

## Przykłady SQL

```sql
SELECT 'databend' REGEXP 'd*', 'databend' RLIKE 'd*';

┌────────────────────────────────────────────────────┐
│ ('databend' regexp 'd*') │ ('databend' rlike 'd*') │
├──────────────────────────┼─────────────────────────┤
│ true                     │ true                    │
└────────────────────────────────────────────────────┘
```
