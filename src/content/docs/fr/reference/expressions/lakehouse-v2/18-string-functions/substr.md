---
title: SUBSTR (Lakehouse v2)
description: SUBSTR — renvoie une sous-chaîne à partir d'une position donnée, avec une longueur facultative.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substr.md
---

Renvoie une sous-chaîne à partir d'une position donnée, avec une longueur facultative.

## Syntaxe Analyze

```python
func.substr(<str>, <pos>[, <len>])
```

## Exemples Analyze

```python
func.substr('StarRocks', 5, 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## Syntaxe SQL

```sql
SUBSTR(<str>, <pos>[, <len>])
```

## Exemples SQL

```sql
SELECT SUBSTR('StarRocks', 5, 5);

┌───────┐
│ Rocks  │
└───────┘
```
