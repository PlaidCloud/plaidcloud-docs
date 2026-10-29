---
title: "LOG(b, x) (Lakehouse v1)"
description: LOG(b, x) – gibt den Logarithmus von x zur Basis b zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logbx.md
---

Gibt den Logarithmus von `x` zur Basis b zurück. Ist `x` kleiner oder gleich 0.0E0, gibt die Funktion NULL zurück.

## Analyze-Syntax

```python
func.log( <b, x> )
```

## Analyze-Beispiele

```python
func.log(2, 65536)

┌────────────────────┐
│ func.log(2, 65536) │
├────────────────────┤
│                 16 │
└────────────────────┘
```

## SQL-Syntax

```sql
LOG( <b, x> )
```

## SQL-Beispiele

```sql
SELECT LOG(2, 65536);

┌───────────────┐
│ log(2, 65536) │
├───────────────┤
│            16 │
└───────────────┘
```
