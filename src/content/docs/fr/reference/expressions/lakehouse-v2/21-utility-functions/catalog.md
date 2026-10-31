---
title: CATALOG (Lakehouse v2)
description: CATALOG — renvoie le nom du catalogue courant.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/catalog.md
---

Renvoie le nom du catalogue courant.

## Syntaxe Analyze

```python
func.catalog()
```

## Exemples Analyze

```python
func.catalog()

┌───────────────────┐
│ 'default_catalog'  │
└───────────────────┘
```

## Syntaxe SQL

```sql
CATALOG()
```

## Exemples SQL

```sql
SELECT CATALOG();

┌─────────────────┐
│ default_catalog  │
└─────────────────┘
```
