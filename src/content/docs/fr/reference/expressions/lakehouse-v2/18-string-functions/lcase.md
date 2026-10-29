---
title: LCASE (Lakehouse v2)
description: LCASE — convertit une chaîne en minuscules. Alias de `LOWER`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lcase.md
---

Convertit une chaîne en minuscules. Alias de `LOWER`.

## Syntaxe Analyze

```python
func.lcase(<str>)
```

## Exemples Analyze

```python
func.lcase('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Syntaxe SQL

```sql
LCASE(<str>)
```

## Exemples SQL

```sql
SELECT LCASE('HELLO');

┌───────┐
│ hello  │
└───────┘
```
