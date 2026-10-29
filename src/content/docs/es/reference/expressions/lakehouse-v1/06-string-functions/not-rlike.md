---
title: NOT RLIKE (Lakehouse v1)
description: NOT RLIKE — devuelve 1 si la cadena expr no coincide con la expresión regular especificada por el patrón pat; de lo contrario, devuelve 0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-rlike.md
---

Devuelve 1 si la cadena expr no coincide con la expresión regular especificada por el patrón pat; de lo contrario, devuelve 0.

## Sintaxis de Analyze

```python
not_(<column>.regexp_match(<pattern>))
```

## Ejemplos de Analyze

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

## Sintaxis SQL

```sql
<expr> NOT RLIKE <pattern>
```

## Ejemplos de SQL

```sql
SELECT 'databend' not rlike 'd*';
┌─────────────────────────────┐
│ ('databend' not rlike 'd*') │
├─────────────────────────────┤
│                           0 │
└─────────────────────────────┘
```
