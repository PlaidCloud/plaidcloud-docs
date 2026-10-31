---
title: IS_NOT_NULL (Lakehouse v1)
description: IS_NOT_NULL — vérifie qu'une valeur n'est pas NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-not-null.md
---

Vérifie qu'une valeur n'est pas NULL.

## Syntaxe Analyze

```python
func.is_not_null(<expr>)
```

## Exemples Analyze

```python
func.is_not_null(1)

┌─────────────────────┐
│ func.is_not_null(1) │
├─────────────────────┤
│ true                │
└─────────────────────┘
```

## Syntaxe SQL

```sql
IS_NOT_NULL(<expr>)
```

## Exemples SQL

```sql
SELECT IS_NOT_NULL(1);

┌────────────────┐
│ is_not_null(1) │
├────────────────┤
│ true           │
└────────────────┘
```
