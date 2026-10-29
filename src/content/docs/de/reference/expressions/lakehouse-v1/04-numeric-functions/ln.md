---
title: LN (Lakehouse v1)
description: LN – gibt den natürlichen Logarithmus von x zurück, also den Logarithmus von x zur Basis e.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ln.md
---

Gibt den natürlichen Logarithmus von `x` zurück, also den Logarithmus von `x` zur Basis e. Ist x kleiner oder gleich 0.0E0, gibt die Funktion NULL zurück.

## Analyze-Syntax

```python
func.ln( <x> )
```

## Analyze-Beispiele

```python
func.ln(2)

┌────────────────────┐
│     func.ln(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## SQL-Syntax

```sql
LN( <x> )
```

## SQL-Beispiele

```sql
SELECT LN(2);

┌────────────────────┐
│        ln(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
