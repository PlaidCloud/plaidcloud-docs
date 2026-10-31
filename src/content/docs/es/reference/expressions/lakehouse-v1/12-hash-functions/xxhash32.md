---
title: XXHASH32 (Lakehouse v1)
description: XXHASH32 calcula un valor hash xxHash32 de 32 bits para una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash32.md
---

Calcula un valor hash xxHash32 de 32 bits para una cadena. El valor se devuelve como UInt32, o NULL si el argumento era NULL.

## Sintaxis de Analyze

```python
func.xxhash32(<expr>)
```

## Ejemplos de Analyze

```python
func.xxhash32('1234567890')

┌─────────────────────────────┐
│ func.xxhash32('1234567890') │
├─────────────────────────────┤
│                  3896585587 │
└─────────────────────────────┘
```

## Sintaxis de SQL

```sql
XXHASH32(<expr>)
```

## Ejemplos de SQL

```sql
SELECT XXHASH32('1234567890');

┌────────────────────────┐
│ xxhash32('1234567890') │
├────────────────────────┤
│             3896585587 │
└────────────────────────┘
```
