---
title: TO_INT16 (Lakehouse v1)
description: "TO_INT16 : convertit une valeur en type de données INT16."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int16.md
---

Convertit une valeur en type de données INT16.

## Syntaxe Analyze

```python
func.to_int16( <expr> )
```

## Exemples Analyze

```python
func.to_int16('123')

┌──────────────────────┐
│ func.to_int16('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Syntaxe SQL

```sql
TO_INT16( <expr> )
```

## Exemples SQL

```sql
SELECT TO_INT16('123');

┌─────────────────┐
│ to_int16('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
