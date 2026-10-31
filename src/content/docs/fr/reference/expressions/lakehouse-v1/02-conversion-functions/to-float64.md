---
title: TO_FLOAT64 (Lakehouse v1)
description: "TO_FLOAT64 : convertit une valeur en type de données FLOAT64."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float64.md
---

Convertit une valeur en type de données FLOAT64.

## Syntaxe Analyze

```python
func.to_float64( <expr> )
```

## Exemples Analyze

```python
func.to_float64('1.2')

┌─────────────────────────┐
│ func.to_float64('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## Syntaxe SQL

```sql
TO_FLOAT64( <expr> )
```

## Exemples SQL

```sql
SELECT TO_FLOAT64('1.2');

┌───────────────────┐
│ to_float64('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```
