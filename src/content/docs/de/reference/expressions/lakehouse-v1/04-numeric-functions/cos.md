---
title: COS (Lakehouse v1)
description: COS – gibt den Kosinus von x zurück, wobei x im Bogenmaß angegeben wird.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cos.md
---

Gibt den Kosinus von `x` zurück, wobei `x` im Bogenmaß angegeben wird.

## Analyze-Syntax

```python
func.cos( <x> )
```

## Analyze-Beispiele

```python
func.cos(func.pi())

┌─────────────────────┐
│ func.cos(func.pi()) │
├─────────────────────┤
│                  -1 │
└─────────────────────┘
```

## SQL-Syntax

```sql
COS( <x> )
```

## SQL-Beispiele

```sql
SELECT COS(PI());

┌───────────┐
│ cos(pi()) │
├───────────┤
│        -1 │
└───────────┘
```
