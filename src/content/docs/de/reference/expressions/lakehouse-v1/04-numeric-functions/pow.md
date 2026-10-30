---
title: POW (Lakehouse v1)
description: POW – gibt den Wert von x potenziert mit y zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/pow.md
---

Gibt den Wert von `x` potenziert mit `y` zurück. 

## Analyze-Syntax

```python
func.pow( <x, y> )
```

## Analyze-Beispiele

```python
func.pow(-2, 2)

┌────────────────────┐
│ func.pow((- 2), 2) │
├────────────────────┤
│                  4 │ 
└────────────────────┘
```

## SQL-Syntax

```sql
POW( <x, y> )
```

## Aliase

- [POWER](../power)

## SQL-Beispiele

```sql
SELECT POW(-2, 2), POWER(-2, 2);

┌─────────────────────────────────┐
│ pow((- 2), 2) │ power((- 2), 2) │
├───────────────┼─────────────────┤
│             4 │               4 │
└─────────────────────────────────┘
```
