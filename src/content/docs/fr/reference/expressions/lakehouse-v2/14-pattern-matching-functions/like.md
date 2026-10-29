---
title: LIKE (Lakehouse v2)
description: "Utilisez la fonction de correspondance de motifs LIKE dans PlaidCloud Lakehouse. Compare une chaîne à un motif à l'aide de `%` (n'importe quels caractères) et de `_` (un seul caractère)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/like.md
---

Compare une chaîne à un motif à l'aide des caractères génériques `%` (n'importe quels caractères) et `_` (un seul caractère).

## Syntaxe Analyze

```python
func.like(<str> LIKE <pattern>)
```

## Exemples Analyze

```python
get_column(table, 'name').like('%alice%')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## Syntaxe SQL

```sql
LIKE(<str> LIKE <pattern>)
```

## Exemples SQL

```sql
SELECT name FROM users WHERE name LIKE '%alice%';

┌─────────────┐
│ alice_smith  │
└─────────────┘
```
