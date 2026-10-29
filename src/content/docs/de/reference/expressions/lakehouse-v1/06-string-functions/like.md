---
title: LIKE (Lakehouse v1)
description: LIKE – Mustervergleich mit einem SQL-Muster.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/like.md
---

Mustervergleich mit einem SQL-Muster. Gibt 1 (TRUE) oder 0 (FALSE) zurück. Ist expr oder pat NULL, ist das Ergebnis NULL.

## Analyze-Syntax

```python
<column>.like('plaid%')
```

## Analyze-Beispiele

```python
my_clothes.like('plaid%)
┌─────────────────┐
│ my_clothes      │
├─────────────────┤
│ plaid pants     │
│ plaid hat       │
│ plaid shirt     │
└─────────────────┘
```

## SQL-Syntax

```sql
<expr> LIKE <pattern>
```

## SQL-Beispiele

```sql
SELECT name, category FROM system.functions WHERE name like 'tou%' ORDER BY name;
┌──────────┬────────────┐
│ name     │ category   │
├──────────┼────────────┤
│ touint16 │ conversion │
│ touint32 │ conversion │
│ touint64 │ conversion │
│ touint8  │ conversion │
└──────────┴────────────┘
```
