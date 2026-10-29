---
title: STARTS_WITH (Lakehouse v2)
description: STARTS_WITH — vérifie si une chaîne commence par un préfixe donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/starts-with.md
---

Vérifie si une chaîne commence par un préfixe donné.

## Syntaxe Analyze

```python
func.starts_with(<str>, <prefix>)
```

## Exemples Analyze

```python
func.starts_with('StarRocks', 'Star')

┌───┐
│ 1  │
└───┘
```

## Syntaxe SQL

```sql
STARTS_WITH(<str>, <prefix>)
```

## Exemples SQL

```sql
SELECT STARTS_WITH('StarRocks', 'Star');

┌───┐
│ 1  │
└───┘
```
