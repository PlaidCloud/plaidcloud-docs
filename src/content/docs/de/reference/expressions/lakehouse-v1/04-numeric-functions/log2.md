---
title: LOG2 (Lakehouse v1)
description: LOG2 – gibt den Logarithmus von x zur Basis 2 zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/log2.md
---

Gibt den Logarithmus von `x` zur Basis 2 zurück. Ist `x` kleiner oder gleich 0.0E0, gibt die Funktion NULL zurück.

## Analyze-Syntax

```python
func.log2( <x> )
```

## Analyze-Beispiele

```python
func.log2(65536)

┌──────────────────┐
│ func.log2(65536) │
├──────────────────┤
│               16 │
└──────────────────┘
```

## SQL-Syntax

```sql
LOG2( <x> )
```

## SQL-Beispiele

```sql
SELECT LOG2(65536);

┌─────────────┐
│ log2(65536) │
├─────────────┤
│          16 │
└─────────────┘
```
