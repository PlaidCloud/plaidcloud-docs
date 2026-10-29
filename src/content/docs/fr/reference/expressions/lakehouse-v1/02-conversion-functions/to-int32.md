---
title: TO_INT32 (Lakehouse v1)
description: "TO_INT32 : convertit une valeur en type de données INT32."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int32.md
---

Convertit une valeur en type de données INT32.

## Syntaxe Analyze

```python
func.to_int32( <expr> )
```

## Exemples Analyze

```python
func.to_int32('123')

┌──────────────────────┐
│ func.to_int32('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Syntaxe SQL

```sql
TO_INT32( <expr> )
```

## Exemples SQL

```sql
SELECT TO_INT32('123');

┌─────────────────┐
│ to_int32('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
