---
title: ENDS_WITH (Lakehouse v2)
description: ENDS_WITH — vérifie si une chaîne se termine par un suffixe donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ends-with.md
---

Vérifie si une chaîne se termine par un suffixe donné.

## Syntaxe Analyze

```python
func.ends_with(<str>, <suffix>)
```

## Exemples Analyze

```python
func.ends_with('hello world', 'world')

┌───┐
│ 1  │
└───┘
```

## Syntaxe SQL

```sql
ENDS_WITH(<str>, <suffix>)
```

## Exemples SQL

```sql
SELECT ENDS_WITH('hello world', 'world');

┌───┐
│ 1  │
└───┘
```
