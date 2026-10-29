---
title: MURMUR_HASH3_32 (Lakehouse v2)
description: MURMUR_HASH3_32 — devuelve el hash MurmurHash3 de 32 bits de un valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/murmur-hash3-32.md
---

Devuelve el hash MurmurHash3 de 32 bits de un valor.

## Sintaxis de Analyze

```python
func.murmur_hash3_32(<expr>[, ...])
```

## Ejemplos de Analyze

```python
func.murmur_hash3_32('hello')

┌───────────┐
│ 613153351  │
└───────────┘
```

## Sintaxis de SQL

```sql
MURMUR_HASH3_32(<expr>[, ...])
```

## Ejemplos de SQL

```sql
SELECT MURMUR_HASH3_32('hello');

┌───────────┐
│ 613153351  │
└───────────┘
```
