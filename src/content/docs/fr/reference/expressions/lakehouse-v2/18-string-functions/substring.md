---
title: SUBSTRING (Lakehouse v2)
description: SUBSTRING — renvoie une sous-chaîne à partir d'une position donnée. Alias de `SUBSTR`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring.md
---

Renvoie une sous-chaîne à partir d'une position donnée. Alias de `SUBSTR`.

## Syntaxe Analyze

```python
func.substring(<str>, <pos>[, <len>])
```

## Exemples Analyze

```python
func.substring('StarRocks', 1, 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## Syntaxe SQL

```sql
SUBSTRING(<str>, <pos>[, <len>])
```

## Exemples SQL

```sql
SELECT SUBSTRING('StarRocks', 1, 4);

┌──────┐
│ Star  │
└──────┘
```
