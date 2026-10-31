---
title: TRIM (Lakehouse v2)
description: TRIM — supprime les espaces de début et de fin ou les caractères spécifiés d'une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/trim.md
---

Supprime les espaces de début et de fin ou les caractères spécifiés d'une chaîne.

## Syntaxe Analyze

```python
func.trim(<str>)
```

## Exemples Analyze

```python
func.trim('  hello  ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Syntaxe SQL

```sql
TRIM(<str>)
```

## Exemples SQL

```sql
SELECT TRIM('  hello  ');

┌───────┐
│ hello  │
└───────┘
```
