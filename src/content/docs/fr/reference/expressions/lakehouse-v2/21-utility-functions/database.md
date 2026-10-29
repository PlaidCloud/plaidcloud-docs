---
title: DATABASE (Lakehouse v2)
description: DATABASE — renvoie le nom de la base de données courante.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/database.md
---

Renvoie le nom de la base de données courante.

## Syntaxe Analyze

```python
func.database()
```

## Exemples Analyze

```python
func.database()

┌───────────────┐
│ 'my_database'  │
└───────────────┘
```

## Syntaxe SQL

```sql
DATABASE()
```

## Exemples SQL

```sql
SELECT DATABASE();

┌─────────────┐
│ my_database  │
└─────────────┘
```
