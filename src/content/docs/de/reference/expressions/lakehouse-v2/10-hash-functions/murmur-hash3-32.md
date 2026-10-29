---
title: MURMUR_HASH3_32 (Lakehouse v2)
description: MURMUR_HASH3_32 – gibt den 32-Bit-MurmurHash3-Hash eines Werts zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/murmur-hash3-32.md
---

Gibt den 32-Bit-MurmurHash3-Hash eines Werts zurück.

## Analyze-Syntax

```python
func.murmur_hash3_32(<expr>[, ...])
```

## Analyze-Beispiele

```python
func.murmur_hash3_32('hello')

┌───────────┐
│ 613153351  │
└───────────┘
```

## SQL-Syntax

```sql
MURMUR_HASH3_32(<expr>[, ...])
```

## SQL-Beispiele

```sql
SELECT MURMUR_HASH3_32('hello');

┌───────────┐
│ 613153351  │
└───────────┘
```
