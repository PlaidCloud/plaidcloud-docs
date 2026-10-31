---
title: NOT RLIKE (Lakehouse v1)
description: NOT RLIKE — devolve 1 se a cadeia de caracteres expr não corresponder à expressão regular especificada pelo padrão pat, e 0 caso contrário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-rlike.md
---

Devolve 1 se a cadeia de caracteres expr não corresponder à expressão regular especificada pelo padrão pat, e 0 caso contrário.

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
<expr> NOT RLIKE <pattern>
```

## Exemplos SQL

```sql
SELECT 'databend' not rlike 'd*';
┌─────────────────────────────┐
│ ('databend' not rlike 'd*') │
├─────────────────────────────┤
│                           0 │
└─────────────────────────────┘
```
