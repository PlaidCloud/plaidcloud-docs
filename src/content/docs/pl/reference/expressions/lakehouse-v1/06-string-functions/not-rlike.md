---
title: NOT RLIKE (Lakehouse v1)
description: NOT RLIKE — zwraca 1, jeśli ciąg znaków expr nie pasuje do wyrażenia regularnego określonego wzorcem pat, w przeciwnym razie 0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-rlike.md
---

Zwraca 1, jeśli ciąg znaków expr nie pasuje do wyrażenia regularnego określonego wzorcem pat, w przeciwnym razie 0.

## Składnia Analyze

```python
not_(<column>.regexp_match(<pattern>))
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

## Składnia SQL

```sql
<expr> NOT RLIKE <pattern>
```

## Przykłady SQL

```sql
SELECT 'databend' not rlike 'd*';
┌─────────────────────────────┐
│ ('databend' not rlike 'd*') │
├─────────────────────────────┤
│                           0 │
└─────────────────────────────┘
```
