---
title: TO_UINT16 (Lakehouse v1)
description: "TO_UINT16 : convertit une valeur en type de données UINT16."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint16.md
---

Convertit une valeur en type de données UINT16.

## Syntaxe Analyze

```python
func.to_uint16( <expr> )
```

## Exemples Analyze

```python
func.to_uint16('123')

┌───────────────────────┐
│ func.to_uint16('123') │
├───────────────────────┤
│                   123 │
└───────────────────────┘
```

## Syntaxe SQL

```sql
TO_UINT16( <expr> )
```

## Exemples SQL

```sql
SELECT TO_UINT16('123');

┌──────────────────┐
│ to_uint16('123') │
├──────────────────┤
│              123 │
└──────────────────┘
```
