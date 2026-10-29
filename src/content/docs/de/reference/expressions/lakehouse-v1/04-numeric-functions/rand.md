---
title: RAND() (Lakehouse v1)
description: RAND() – gibt einen zufälligen Gleitkommawert v im Bereich 0 <= v < 1 zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/rand.md
---

Gibt einen zufälligen Gleitkommawert v im Bereich 0 &lt;= v &lt; 1.0 zurück. Um eine zufällige ganze Zahl R im Bereich i &lt;= R &lt; j zu erhalten, verwenden Sie den Ausdruck FLOOR(i + RAND() * (j − i)).

## Analyze-Syntax

```python
func.rand()
```

## Analyze-Beispiele

```python
func.rand()

┌────────────────────┐
│    func.rand()     │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```

## SQL-Syntax

```sql
RAND()
```

## SQL-Beispiele

```sql
SELECT RAND();

┌────────────────────┐
│       rand()       │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```
