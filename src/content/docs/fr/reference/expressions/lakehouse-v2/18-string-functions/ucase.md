---
title: UCASE (Lakehouse v2)
description: UCASE — convertit une chaîne en majuscules. Alias de `UPPER`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ucase.md
---

Convertit une chaîne en majuscules. Alias de `UPPER`.

## Syntaxe Analyze

```python
func.ucase(<str>)
```

## Exemples Analyze

```python
func.ucase('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## Syntaxe SQL

```sql
UCASE(<str>)
```

## Exemples SQL

```sql
SELECT UCASE('hello');

┌───────┐
│ HELLO  │
└───────┘
```
