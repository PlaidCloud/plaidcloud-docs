---
title: BLAKE3 (Lakehouse v1)
description: BLAKE3 calcula una suma de comprobación BLAKE3 de 256 bits para una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/blake3.md
---

Calcula una suma de comprobación BLAKE3 de 256 bits para una cadena. El valor se devuelve como una cadena de 64 dígitos hexadecimales, o NULL si el argumento era NULL.

## Sintaxis de Analyze

```python
func.blake3(<expr>)
```

## Ejemplos de Analyze

```python
func.blake3('1234567890')

┌──────────────────────────────────────────────────────────────────┐
│ func.blake3('1234567890')                                        │
├──────────────────────────────────────────────────────────────────┤
│ d12e417e04494572b561ba2c12c3d7f9e5107c4747e27b9a8a54f8480c63e841 │
└──────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BLAKE3(<expr>)
```

## Ejemplos de SQL

```sql
SELECT BLAKE3('1234567890');

┌──────────────────────────────────────────────────────────────────┐
│                       blake3('1234567890')                       │
├──────────────────────────────────────────────────────────────────┤
│ d12e417e04494572b561ba2c12c3d7f9e5107c4747e27b9a8a54f8480c63e841 │
└──────────────────────────────────────────────────────────────────┘
```
