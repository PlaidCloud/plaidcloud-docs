---
title: TO_FLOAT32 (Lakehouse v1)
description: "TO_FLOAT32 : convertit une valeur en type de données FLOAT32."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-float32.md
---

Convertit une valeur en type de données FLOAT32.

## Syntaxe Analyze

```python
func.to_float32( <expr> )
```

## Exemples Analyze

```python
func.to_float32('1.2')

┌─────────────────────────┐
│ func.to_float32('1.2')  │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## Syntaxe SQL

```sql
TO_FLOAT32( <expr> )
```

## Exemples SQL

```sql
SELECT TO_FLOAT32('1.2');

┌───────────────────┐
│ to_float32('1.2') │
├───────────────────┤
│               1.2 │
└───────────────────┘
```
