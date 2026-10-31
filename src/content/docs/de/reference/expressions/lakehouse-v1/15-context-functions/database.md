---
title: DATABASE (Lakehouse v1)
description: DATABASE gibt den Namen der aktuell ausgewählten Datenbank zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/database.md
---

Gibt den Namen der aktuell ausgewählten Datenbank zurück. Ist keine Datenbank ausgewählt, gibt diese Funktion `default` zurück.

## Analyze-Syntax

```python
func.database()
```

## Analyze-Beispiele

```python
func.database()

┌─────────────────┐
│ func.database() │
├─────────────────┤
│ default         │
└─────────────────┘
```

## SQL-Syntax

```sql
DATABASE()
```

## SQL-Beispiele

```sql
SELECT DATABASE();

┌────────────┐
│ database() │
├────────────┤
│ default    │
└────────────┘
```
