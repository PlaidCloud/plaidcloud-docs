---
title: LOG10 (Lakehouse v1)
description: LOG10 – gibt den Logarithmus von x zur Basis 10 zurück. Referenz.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log10.md
---

Gibt den Logarithmus von `x` zur Basis 10 zurück. Ist `x` kleiner oder gleich 0.0E0, gibt die Funktion NULL zurück.


## Analyze-Syntax

```python
func.log10( <x> )
```

## Analyze-Beispiele

```python
func.log10(100)

┌─────────────────┐
│ func.log10(100) │
├─────────────────┤
│               2 │
└─────────────────┘
```

## SQL-Syntax

```sql
LOG10( <x> )
```

## SQL-Beispiele

```sql
SELECT LOG10(100);

┌────────────┐
│ log10(100) │
├────────────┤
│          2 │
└────────────┘
```
