---
title: XXHASH64 (Lakehouse v1)
description: XXHASH64 — calcula um valor de hash xxHash64 de 64 bits para uma cadeia de caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash64.md
---

Calcula um valor de hash xxHash64 de 64 bits para uma cadeia de caracteres. O valor é devolvido como UInt64 ou NULL se o argumento for NULL.

## Sintaxe do Analyze

```python
func.xxhash64(<expr>)
```

## Exemplos do Analyze

```python
func.xxhash64('1234567890')

┌─────────────────────────────┐
│ func.xxhash64('1234567890') │
├─────────────────────────────┤
│        12237639266330420150 │
└─────────────────────────────┘
```

## Sintaxe SQL

```sql
XXHASH64(<expr>)
```

## Exemplos de SQL

```sql
SELECT XXHASH64('1234567890');

┌────────────────────────┐
│ xxhash64('1234567890') │
├────────────────────────┤
│   12237639266330420150 │
└────────────────────────┘
```
