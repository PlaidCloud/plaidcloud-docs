---
title: BLAKE3 (Lakehouse v1)
description: BLAKE3 — calcula uma soma de verificação BLAKE3 de 256 bits para uma string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/blake3.md
---

Calcula uma soma de verificação BLAKE3 de 256 bits para uma string. O valor é retornado como uma string de 64 dígitos hexadecimais ou NULL se o argumento for NULL.

## Sintaxe no Analyze

```python
func.blake3(<expr>)
```

## Exemplos no Analyze

```python
func.blake3('1234567890')

┌──────────────────────────────────────────────────────────────────┐
│ func.blake3('1234567890')                                        │
├──────────────────────────────────────────────────────────────────┤
│ d12e417e04494572b561ba2c12c3d7f9e5107c4747e27b9a8a54f8480c63e841 │
└──────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
BLAKE3(<expr>)
```

## Exemplos de SQL

```sql
SELECT BLAKE3('1234567890');

┌──────────────────────────────────────────────────────────────────┐
│                       blake3('1234567890')                       │
├──────────────────────────────────────────────────────────────────┤
│ d12e417e04494572b561ba2c12c3d7f9e5107c4747e27b9a8a54f8480c63e841 │
└──────────────────────────────────────────────────────────────────┘
```
