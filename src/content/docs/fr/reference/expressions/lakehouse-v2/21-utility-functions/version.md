---
title: VERSION (Lakehouse v2)
description: VERSION — renvoie la version du protocole MySQL de StarRocks.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/version.md
---

Renvoie la version du protocole MySQL de StarRocks.

## Syntaxe Analyze

```python
func.version()
```

## Exemples Analyze

```python
func.version()

┌─────────┐
│ '5.1.0'  │
└─────────┘
```

## Syntaxe SQL

```sql
VERSION()
```

## Exemples SQL

```sql
SELECT VERSION();

┌───────┐
│ 5.1.0  │
└───────┘
```
