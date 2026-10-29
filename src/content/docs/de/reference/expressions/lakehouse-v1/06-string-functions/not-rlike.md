---
title: NOT RLIKE (Lakehouse v1)
description: NOT RLIKE – gibt 1 zurück, wenn die Zeichenfolge expr nicht zum durch das Muster pat angegebenen regulären Ausdruck passt, andernfalls 0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-rlike.md
---

Gibt 1 zurück, wenn die Zeichenfolge expr nicht zum durch das Muster pat angegebenen regulären Ausdruck passt, andernfalls 0.

## Analyze-Syntax

```python
not_(<column>.regexp_match(<pattern>))
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

## SQL-Syntax

```sql
<expr> NOT RLIKE <pattern>
```

## SQL-Beispiele

```sql
SELECT 'databend' not rlike 'd*';
┌─────────────────────────────┐
│ ('databend' not rlike 'd*') │
├─────────────────────────────┤
│                           0 │
└─────────────────────────────┘
```
