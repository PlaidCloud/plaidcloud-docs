---
title: SIN (Lakehouse v1)
description: SIN – gibt den Sinus von x zurück, wobei x im Bogenmaß angegeben wird.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sin.md
---

Gibt den Sinus von `x` zurück, wobei `x` im Bogenmaß angegeben wird.

## Analyze-Syntax

```python
func.sin( <x> )
```

## Analyze-Beispiele

```python
func.sin(90)

┌────────────────────┐
│    func.sin(90)    │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```

## SQL-Syntax

```sql
SIN( <x> )
```

## SQL-Beispiele

```sql
SELECT SIN(90);

┌────────────────────┐
│       sin(90)      │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```
