---
title: BLAKE3 (Lakehouse v1)
description: BLAKE3 — oblicza 256-bitową sumę kontrolną BLAKE3 dla ciągu znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/blake3.md
---

Oblicza 256-bitową sumę kontrolną BLAKE3 dla ciągu znaków. Wartość jest zwracana jako ciąg 64 cyfr szesnastkowych lub NULL, jeśli argument miał wartość NULL.

## Składnia Analyze

```python
func.blake3(<expr>)
```

## Przykłady Analyze

```python
func.blake3('1234567890')

┌──────────────────────────────────────────────────────────────────┐
│ func.blake3('1234567890')                                        │
├──────────────────────────────────────────────────────────────────┤
│ d12e417e04494572b561ba2c12c3d7f9e5107c4747e27b9a8a54f8480c63e841 │
└──────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
BLAKE3(<expr>)
```

## Przykłady SQL

```sql
SELECT BLAKE3('1234567890');

┌──────────────────────────────────────────────────────────────────┐
│                       blake3('1234567890')                       │
├──────────────────────────────────────────────────────────────────┤
│ d12e417e04494572b561ba2c12c3d7f9e5107c4747e27b9a8a54f8480c63e841 │
└──────────────────────────────────────────────────────────────────┘
```
