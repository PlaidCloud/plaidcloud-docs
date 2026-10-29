---
title: NOT REGEXP (Lakehouse v1)
description: NOT REGEXP — retorna 1 se a string expr não corresponder à expressão regular especificada pelo padrão pat; caso contrário, retorna 0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-regexp.md
---

Retorna 1 se a string expr não corresponder à expressão regular especificada pelo padrão pat; caso contrário, retorna 0.

## Sintaxe do Analyze

```python
not_(<column>.regexp_match(<pattern>))
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

## Sintaxe SQL

```sql
<expr> NOT REGEXP <pattern>
```

## Exemplos de SQL

```sql
SELECT 'databend' NOT REGEXP 'd*';
┌──────────────────────────────┐
│ ('databend' not regexp 'd*') │
├──────────────────────────────┤
│                            0 │
└──────────────────────────────┘
```
