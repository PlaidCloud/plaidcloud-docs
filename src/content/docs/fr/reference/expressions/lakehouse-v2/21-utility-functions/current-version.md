---
title: CURRENT_VERSION (Lakehouse v2)
description: CURRENT_VERSION — renvoie la version courante de StarRocks.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-version.md
---

Renvoie la version courante de StarRocks.

## Syntaxe Analyze

```python
func.current_version()
```

## Exemples Analyze

```python
func.current_version()

┌─────────┐
│ '4.1.0'  │
└─────────┘
```

## Syntaxe SQL

```sql
CURRENT_VERSION()
```

## Exemples SQL

```sql
SELECT CURRENT_VERSION();

┌──────────────┐
│ 4.1.0-xxxxxx  │
└──────────────┘
```
