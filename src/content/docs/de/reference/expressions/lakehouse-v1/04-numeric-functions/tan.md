---
title: TAN (Lakehouse v1)
description: TAN – gibt den Tangens von x zurück, wobei x im Bogenmaß angegeben wird.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/tan.md
---

Gibt den Tangens von `x` zurück, wobei `x` im Bogenmaß angegeben wird.

## Analyze-Syntax

```python
func.tan( <x> )
```

## Analyze-Beispiele

```python
func.tan(90)

┌────────────────────┐
│    func.tan(90)    │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```

## SQL-Syntax

```sql
TAN( <x> )
```

## SQL-Beispiele

```sql
SELECT TAN(90);

┌────────────────────┐
│       tan(90)      │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```
