---
title: CURRENT_WAREHOUSE (Lakehouse v2)
description: CURRENT_WAREHOUSE — renvoie le nom de l'entrepôt courant.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-warehouse.md
---

Renvoie le nom de l'entrepôt courant.

## Syntaxe Analyze

```python
func.current_warehouse()
```

## Exemples Analyze

```python
func.current_warehouse()

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```

## Syntaxe SQL

```sql
CURRENT_WAREHOUSE()
```

## Exemples SQL

```sql
SELECT CURRENT_WAREHOUSE();

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```
