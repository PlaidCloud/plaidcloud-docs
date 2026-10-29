---
title: TO_UINT64 (Lakehouse v1)
description: "TO_UINT64 : convertit une valeur en type de données UINT64."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint64.md
---

Convertit une valeur en type de données UINT64.

## Syntaxe Analyze

```python
func.to_uint64( <expr> )
```

## Exemples Analyze

```python
func.to_uint64('123')

┌───────────────────────┐
│ func.to_uint64('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## Syntaxe SQL

```sql
TO_UINT64( <expr> )
```

## Exemples SQL

```sql
SELECT TO_UINT64('123');

┌──────────────────┐
│ to_uint64('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
