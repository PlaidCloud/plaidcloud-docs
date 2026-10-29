---
title: XXHASH64 (Lakehouse v1)
description: XXHASH64 — oblicza 64-bitową wartość skrótu xxHash64 dla ciągu znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash64.md
---

Oblicza 64-bitową wartość skrótu xxHash64 dla ciągu znaków. Wartość jest zwracana jako UInt64 lub NULL, jeśli argument miał wartość NULL.

## Składnia Analyze

```python
func.xxhash64(<expr>)
```

## Przykłady Analyze

```python
func.xxhash64('1234567890')

┌─────────────────────────────┐
│ func.xxhash64('1234567890') │
├─────────────────────────────┤
│        12237639266330420150 │
└─────────────────────────────┘
```

## Składnia SQL

```sql
XXHASH64(<expr>)
```

## Przykłady SQL

```sql
SELECT XXHASH64('1234567890');

┌────────────────────────┐
│ xxhash64('1234567890') │
├────────────────────────┤
│   12237639266330420150 │
└────────────────────────┘
```
