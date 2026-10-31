---
title: LOWER (Lakehouse v2)
description: LOWER — convertit une chaîne en minuscules.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lower.md
---

Convertit une chaîne en minuscules.

## Syntaxe Analyze

```python
func.lower(<str>)
```

## Exemples Analyze

```python
func.lower('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Syntaxe SQL

```sql
LOWER(<str>)
```

## Exemples SQL

```sql
SELECT LOWER('HELLO');

┌───────┐
│ hello  │
└───────┘
```
