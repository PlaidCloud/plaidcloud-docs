---
title: DATABASE (Lakehouse v1)
description: DATABASE — renvoie le nom de la base de données actuellement sélectionnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/database.md
---

Renvoie le nom de la base de données actuellement sélectionnée. Si aucune base de données n'est sélectionnée, cette fonction renvoie `default`.

## Syntaxe Analyze

```python
func.database()
```

## Exemples Analyze

```python
func.database()

┌─────────────────┐
│ func.database() │
├─────────────────┤
│ default         │
└─────────────────┘
```

## Syntaxe SQL

```sql
DATABASE()
```

## Exemples SQL

```sql
SELECT DATABASE();

┌────────────┐
│ database() │
├────────────┤
│ default    │
└────────────┘
```
