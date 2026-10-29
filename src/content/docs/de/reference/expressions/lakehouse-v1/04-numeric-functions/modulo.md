---
title: MODULO (Lakehouse v1)
description: MODULO – gibt den Rest der Division von x durch y zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/modulo.md
---

Gibt den Rest der Division von `x` durch `y` zurück. Ist `y` gleich 0, wird ein Fehler zurückgegeben.

## Analyze-Syntax

```python
func.modulo( <x>, <y> )
```

## Analyze-Beispiele

```python
func.modulo(9, 2)

┌───────────────────┐
│ func.modulo(9, 2) │
├───────────────────┤
│                 1 │
└───────────────────┘
```

## SQL-Syntax

```sql
MODULO( <x>, <y> )
```

## Aliase

- [MOD](../mod)

## SQL-Beispiele

```sql
SELECT MOD(9, 2), MODULO(9, 2);

┌──────────────────────────┐
│ mod(9, 2) │ modulo(9, 2) │
├───────────┼──────────────┤
│         1 │            1 │
└──────────────────────────┘
```
