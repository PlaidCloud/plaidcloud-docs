---
title: XXHASH32 (Lakehouse v1)
description: XXHASH32 — calcula um valor de hash xxHash32 de 32 bits para uma cadeia de caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash32.md
---

Calcula um valor de hash xxHash32 de 32 bits para uma cadeia de caracteres. O valor é devolvido como UInt32 ou NULL se o argumento for NULL.

## Sintaxe do Analyze

```python
func.xxhash32(<expr>)
```

## Exemplos do Analyze

```python
func.xxhash32('1234567890')

┌─────────────────────────────┐
│ func.xxhash32('1234567890') │
├─────────────────────────────┤
│                  3896585587 │
└─────────────────────────────┘
```

## Sintaxe SQL

```sql
XXHASH32(<expr>)
```

## Exemplos de SQL

```sql
SELECT XXHASH32('1234567890');

┌────────────────────────┐
│ xxhash32('1234567890') │
├────────────────────────┤
│             3896585587 │
└────────────────────────┘
```
