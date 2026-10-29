---
title: "REVERSE (String, Lakehouse v2)"
description: REVERSE — inverse l'ordre des caractères d'une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/reverse.md
---

Inverse l'ordre des caractères d'une chaîne.

## Syntaxe Analyze

```python
func.reverse(<str>)
```

## Exemples Analyze

```python
func.reverse('hello')

┌─────────┐
│ 'olleh'  │
└─────────┘
```

## Syntaxe SQL

```sql
REVERSE(<str>)
```

## Exemples SQL

```sql
SELECT REVERSE('hello');

┌───────┐
│ olleh  │
└───────┘
```
