---
title: TO_BITMAP (Lakehouse v1)
description: "TO_BITMAP : convertit une valeur en type de données BITMAP."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-bitmap.md
---

Convertit une valeur en type de données BITMAP.

## Syntaxe Analyze

```python
func.to_bitmap( <expr> )
```

## Exemples Analyze

```python
func.to_bitmap('1101')

┌─────────────────────────┐
│ func.to_bitmap('1101')  │
├─────────────────────────┤
│ <bitmap binary>         │
└─────────────────────────┘
```

## Syntaxe SQL

```sql
TO_BITMAP( <expr> )
```

## Exemples SQL

```sql
SELECT TO_BITMAP('1101');

┌───────────────────┐
│ to_bitmap('1101') │
├───────────────────┤
│ <bitmap binary>   │
└───────────────────┘
```
