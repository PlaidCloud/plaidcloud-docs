---
title: UPPER (Lakehouse v2)
description: UPPER — convertit une chaîne en majuscules.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/upper.md
---

Convertit une chaîne en majuscules.

## Syntaxe Analyze

```python
func.upper(<str>)
```

## Exemples Analyze

```python
func.upper('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## Syntaxe SQL

```sql
UPPER(<str>)
```

## Exemples SQL

```sql
SELECT UPPER('hello');

┌───────┐
│ HELLO  │
└───────┘
```
