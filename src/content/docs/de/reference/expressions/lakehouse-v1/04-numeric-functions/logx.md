---
title: LOG(x) (Lakehouse v1)
description: LOG(x) – gibt den natürlichen Logarithmus von x zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/logx.md
---

Gibt den natürlichen Logarithmus von `x` zurück. Ist x kleiner oder gleich 0.0E0, gibt die Funktion NULL zurück.

## Analyze-Syntax

```python
 func.log( <x> )
```

## Analyze-Beispiele

```python
 func.log(2)

┌────────────────────┐
│    func.log(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## SQL-Syntax

```sql
LOG( <x> )
```

## SQL-Beispiele

```sql
SELECT LOG(2);

┌────────────────────┐
│       log(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
