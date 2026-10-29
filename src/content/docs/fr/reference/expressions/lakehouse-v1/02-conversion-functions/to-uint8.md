---
title: TO_UINT8 (Lakehouse v1)
description: "TO_UINT8 : convertit une valeur en type de données UINT8."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-uint8.md
---

Convertit une valeur en type de données UINT8.

## Syntaxe Analyze

```python
func.to_uint8( <expr> )
```

## Exemples Analyze

```python
func.to_uint8('123')

┌──────────────────────┐
│ func.to_uint8('123') │
├──────────────────────┤
│                  123 │
└──────────────────────┘
```

## Syntaxe SQL

```sql
TO_UINT8( <expr> )
```

## Exemples SQL

```sql
SELECT TO_UINT8('123');

┌─────────────────┐
│ to_uint8('123') │
├─────────────────┤
│             123 │
└─────────────────┘
```
