---
title: XXHASH64 (Lakehouse v1)
description: XXHASH64 calcula un valor hash xxHash64 de 64 bits para una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash64.md
---

Calcula un valor hash xxHash64 de 64 bits para una cadena. El valor se devuelve como UInt64, o NULL si el argumento era NULL.

## Sintaxis de Analyze

```python
func.xxhash64(<expr>)
```

## Ejemplos de Analyze

```python
func.xxhash64('1234567890')

┌─────────────────────────────┐
│ func.xxhash64('1234567890') │
├─────────────────────────────┤
│        12237639266330420150 │
└─────────────────────────────┘
```

## Sintaxis de SQL

```sql
XXHASH64(<expr>)
```

## Ejemplos de SQL

```sql
SELECT XXHASH64('1234567890');

┌────────────────────────┐
│ xxhash64('1234567890') │
├────────────────────────┤
│   12237639266330420150 │
└────────────────────────┘
```
