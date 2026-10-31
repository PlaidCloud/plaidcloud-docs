---
title: DATABASE (Lakehouse v2)
description: DATABASE — gibt den Namen der aktuellen Datenbank zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/database.md
---

Gibt den Namen der aktuellen Datenbank zurück.

## Analyze-Syntax

```python
func.database()
```

## Analyze-Beispiele

```python
func.database()

┌───────────────┐
│ 'my_database'  │
└───────────────┘
```

## SQL-Syntax

```sql
DATABASE()
```

## SQL-Beispiele

```sql
SELECT DATABASE();

┌─────────────┐
│ my_database  │
└─────────────┘
```
