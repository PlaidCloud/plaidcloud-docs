---
title: FACTORIAL (Lakehouse v1)
description: FACTORIAL – gibt die Fakultät von x zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/factorial.md
---

Gibt die Fakultät von `x` zurück. Ist `x` kleiner oder gleich 0, gibt die Funktion 0 zurück.

## Analyze-Syntax

```python
func.factorial( <x> )
```

## Analyze-Beispiele

```python
func.factorial(5)

┌───────────────────┐
│ func.factorial(5) │
├───────────────────┤
│               120 │
└───────────────────┘
```

## SQL-Syntax

```sql
FACTORIAL( <x> )
```

## SQL-Beispiele

```sql
SELECT FACTORIAL(5);

┌──────────────┐
│ factorial(5) │
├──────────────┤
│          120 │
└──────────────┘
```
