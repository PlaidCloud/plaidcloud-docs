---
title: COT (Lakehouse v1)
description: COT – gibt den Kotangens von x zurück, wobei x im Bogenmaß angegeben wird.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cot.md
---

Gibt den Kotangens von `x` zurück, wobei `x` im Bogenmaß angegeben wird.

## Analyze-Syntax

```python
func.cot( <x> )
```

## Analyze-Beispiele

```python
func.cot(12) 

┌─────────────────────┐
│    func.cot(12)     │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```

## SQL-Syntax

```sql
COT( <x> )
```

## SQL-Beispiele

```sql
SELECT COT(12);

┌─────────────────────┐
│       cot(12)       │
├─────────────────────┤
│ -1.5726734063976895 │
└─────────────────────┘
```
