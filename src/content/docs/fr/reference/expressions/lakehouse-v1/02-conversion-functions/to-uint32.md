---
title: TO_UINT32 (Lakehouse v1)
description: "TO_UINT32 : convertit une valeur en type de données UINT32."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint32.md
---

Convertit une valeur en type de données UINT32.

## Syntaxe Analyze

```python
func.to_uint32( <expr> )
```

## Exemples Analyze

```python
func.to_uint32('123')

┌───────────────────────┐
│ func.to_uint32('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## Syntaxe SQL

```sql
TO_UINT32( <expr> )
```

## Exemples SQL

```sql
SELECT TO_UINT32('123');

┌──────────────────┐
│ to_uint32('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
