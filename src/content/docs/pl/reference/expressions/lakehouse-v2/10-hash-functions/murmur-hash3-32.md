---
title: MURMUR_HASH3_32 (Lakehouse v2)
description: MURMUR_HASH3_32 — zwraca 32-bitowy skrót MurmurHash3 wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/murmur-hash3-32.md
---

Zwraca 32-bitowy skrót MurmurHash3 wartości.

## Składnia Analyze

```python
func.murmur_hash3_32(<expr>[, ...])
```

## Przykłady Analyze

```python
func.murmur_hash3_32('hello')

┌───────────┐
│ 613153351  │
└───────────┘
```

## Składnia SQL

```sql
MURMUR_HASH3_32(<expr>[, ...])
```

## Przykłady SQL

```sql
SELECT MURMUR_HASH3_32('hello');

┌───────────┐
│ 613153351  │
└───────────┘
```
