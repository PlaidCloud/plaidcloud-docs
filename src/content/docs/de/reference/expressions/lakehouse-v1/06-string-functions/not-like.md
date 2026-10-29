---
title: NOT LIKE (Lakehouse v1)
description: NOT LIKE – Ausschluss per Mustervergleich mit einem SQL-Muster.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/not-like.md
---

Ausschluss per Mustervergleich mit einem SQL-Muster. Gibt 1 (TRUE) oder 0 (FALSE) zurück. Ist expr oder pat NULL, ist das Ergebnis NULL.

## Analyze-Syntax

```python
<column>.not_like(<pattern>)
```

## Analyze-Beispiele

```python
my_clothes.not_like('%pants)
┌─────────────────┐
│ my_clothes      │
├─────────────────┤
│ plaid pants XL  │
│ plaid hat       │
│ plaid shirt     │
└─────────────────┘
```

## SQL-Syntax

```sql
<expr> NOT LIKE <pattern>
```

## SQL-Beispiele

```sql
SELECT name, category FROM system.functions WHERE name like 'tou%' AND name not like '%64' ORDER BY name;
┌──────────┬────────────┐
│ name     │ category   │
├──────────┼────────────┤
│ touint16 │ conversion │
│ touint32 │ conversion │
│ touint8  │ conversion │
└──────────┴────────────┘
```
