---
title: CURRENT_ROLE (Lakehouse v2)
description: CURRENT_ROLE — gibt die aktuell aktive Rolle zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-role.md
---

Gibt die aktuell aktive Rolle zurück.

## Analyze-Syntax

```python
func.current_role()
```

## Analyze-Beispiele

```python
func.current_role()

┌─────────┐
│ 'admin'  │
└─────────┘
```

## SQL-Syntax

```sql
CURRENT_ROLE()
```

## SQL-Beispiele

```sql
SELECT CURRENT_ROLE();

┌───────┐
│ admin  │
└───────┘
```
