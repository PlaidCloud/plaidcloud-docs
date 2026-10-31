---
title: TO_INT8 (Lakehouse v1)
description: "TO_INT8 : convertit une valeur en type de données INT8."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-int8.md
---

Convertit une valeur en type de données INT8.

## Syntaxe Analyze

```python
func.to_int8( <expr> )
```

## Exemples Analyze

```python
func.to_int8('123')

┌─────────────────────┐
│ func.to_int8('123') │
├─────────────────────┤
│                 123 │
└─────────────────────┘
```

## Syntaxe SQL

```sql
TO_INT8( <expr> )
```

## Exemples SQL

```sql
SELECT TO_INT8('123');

┌────────────────┐
│ to_int8('123') │
│      UInt8     │
├────────────────┤
│            123 │
└────────────────┘
```
