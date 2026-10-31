---
title: LTRIM (Lakehouse v2)
description: LTRIM — supprime les espaces de début ou les caractères spécifiés au début d'une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ltrim.md
---

Supprime les espaces de début ou les caractères spécifiés au début d'une chaîne.

## Syntaxe Analyze

```python
func.ltrim(<str>)
```

## Exemples Analyze

```python
func.ltrim('   hello')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Syntaxe SQL

```sql
LTRIM(<str>)
```

## Exemples SQL

```sql
SELECT LTRIM('   hello');

┌───────┐
│ hello  │
└───────┘
```
