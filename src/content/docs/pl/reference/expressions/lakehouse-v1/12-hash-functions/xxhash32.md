---
title: XXHASH32 (Lakehouse v1)
description: XXHASH32 — oblicza 32-bitową wartość skrótu xxHash32 dla ciągu znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash32.md
---

Oblicza 32-bitową wartość skrótu xxHash32 dla ciągu znaków. Wartość jest zwracana jako UInt32 lub NULL, jeśli argument miał wartość NULL.

## Składnia Analyze

```python
func.xxhash32(<expr>)
```

## Przykłady Analyze

```python
func.xxhash32('1234567890')

┌─────────────────────────────┐
│ func.xxhash32('1234567890') │
├─────────────────────────────┤
│                  3896585587 │
└─────────────────────────────┘
```

## Składnia SQL

```sql
XXHASH32(<expr>)
```

## Przykłady SQL

```sql
SELECT XXHASH32('1234567890');

┌────────────────────────┐
│ xxhash32('1234567890') │
├────────────────────────┤
│             3896585587 │
└────────────────────────┘
```
