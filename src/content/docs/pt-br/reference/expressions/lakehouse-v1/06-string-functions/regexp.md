---
title: REGEXP (Lakehouse v1)
description: REGEXP — retorna true se a string <expr> corresponder à expressão regular especificada por <pattern>; caso contrário, retorna false.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp.md
---

Retorna `true` se a string `<expr>` corresponder à expressão regular especificada por `<pattern>`; caso contrário, retorna `false`.

## Sintaxe do Analyze

```python
<column>.regexp_match(<pattern>)
```

## Exemplos do Analyze

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

## Sintaxe SQL

```sql
<expr> REGEXP <pattern>
```

## Aliases

- [RLIKE](../rlike)

## Exemplos de SQL

```sql
SELECT 'databend' REGEXP 'd*', 'databend' RLIKE 'd*';

┌────────────────────────────────────────────────────┐
│ ('databend' regexp 'd*') │ ('databend' rlike 'd*') │
├──────────────────────────┼─────────────────────────┤
│ true                     │ true                    │
└────────────────────────────────────────────────────┘
```
