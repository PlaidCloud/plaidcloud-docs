---
title: NOT REGEXP (Lakehouse v1)
description: NOT REGEXP renvoie 1 si la chaîne expr ne correspond pas à l'expression régulière définie par le motif pat, sinon 0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-regexp.md
---

Renvoie 1 si la chaîne expr ne correspond pas à l'expression régulière définie par le motif pat, sinon 0.

## Syntaxe Analyze

```python
not_(<column>.regexp_match(<pattern>))
```

## Exemples Analyze

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

## Syntaxe SQL

```sql
<expr> NOT REGEXP <pattern>
```

## Exemples SQL

```sql
SELECT 'databend' NOT REGEXP 'd*';
┌──────────────────────────────┐
│ ('databend' not regexp 'd*') │
├──────────────────────────────┤
│                            0 │
└──────────────────────────────┘
```
