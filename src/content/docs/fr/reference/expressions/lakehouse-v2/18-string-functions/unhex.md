---
title: UNHEX (Lakehouse v2)
description: UNHEX — convertit une chaîne hexadécimale en chaîne de caractères.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/unhex.md
---

Convertit une chaîne hexadécimale en chaîne de caractères.

## Syntaxe Analyze

```python
func.unhex(<hex_str>)
```

## Exemples Analyze

```python
func.unhex('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Syntaxe SQL

```sql
UNHEX(<hex_str>)
```

## Exemples SQL

```sql
SELECT UNHEX('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
