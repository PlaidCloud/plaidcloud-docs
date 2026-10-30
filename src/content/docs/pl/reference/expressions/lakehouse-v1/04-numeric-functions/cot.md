---
title: COT (Lakehouse v1)
description: COT — zwraca cotangens x, gdzie x jest podane w radianach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cot.md
---

Zwraca cotangens `x`, gdzie `x` jest podane w radianach.

## Składnia Analyze

```python
func.cot( <x> )
```

## Przykłady Analyze

```python
func.cot(12) 

┌─────────────────────┐
│    func.cot(12)     │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```

## Składnia SQL

```sql
COT( <x> )
```

## Przykłady SQL

```sql
SELECT COT(12);

┌─────────────────────┐
│       cot(12)       │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```
