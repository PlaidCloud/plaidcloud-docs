---
title: TO_INT64 (Lakehouse v1)
description: "TO_INT64 : convertit une valeur en type de données INT64."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int64.md
---

Convertit une valeur en type de données INT64.

## Syntaxe Analyze

```python
func.to_int64( <expr> )
```

## Exemples Analyze

```python
func.to_int64('123')

┌──────────────────────┐
│ func.to_int64('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Syntaxe SQL

```sql
TO_INT64( <expr> )
```

## Exemples SQL

```sql
SELECT TO_INT64('123');

┌─────────────────┐
│ to_int64('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
