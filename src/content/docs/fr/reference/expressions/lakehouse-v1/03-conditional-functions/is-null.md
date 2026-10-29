---
title: IS_NULL (Lakehouse v1)
description: IS_NULL — vérifie si une valeur est NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-null.md
---

Vérifie si une valeur est NULL.

## Syntaxe Analyze

```python
func.is_null(<expr>)
```

## Exemples Analyze

```python
func.is_null(1)

┌─────────────────┐
│ func.is_null(1) │
├─────────────────┤
│ false           │
└─────────────────┘
```

## Syntaxe SQL

```sql
IS_NULL(<expr>)
```

## Exemples SQL

```sql
SELECT IS_NULL(1);

┌────────────┐
│ is_null(1) │
├────────────┤
│ false      │
└────────────┘
```
