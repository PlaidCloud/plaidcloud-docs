---
title: CURRENT_ROLE (Lakehouse v2)
description: CURRENT_ROLE — renvoie le rôle actif courant.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-role.md
---

Renvoie le rôle actif courant.

## Syntaxe Analyze

```python
func.current_role()
```

## Exemples Analyze

```python
func.current_role()

┌─────────┐
│ 'admin'  │
└─────────┘
```

## Syntaxe SQL

```sql
CURRENT_ROLE()
```

## Exemples SQL

```sql
SELECT CURRENT_ROLE();

┌───────┐
│ admin  │
└───────┘
```
