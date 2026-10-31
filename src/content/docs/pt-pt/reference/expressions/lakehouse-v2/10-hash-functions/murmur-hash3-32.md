---
title: MURMUR_HASH3_32 (Lakehouse v2)
description: MURMUR_HASH3_32 — devolve o hash MurmurHash3 de 32 bits de um valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/murmur-hash3-32.md
---

Devolve o hash MurmurHash3 de 32 bits de um valor.

## Sintaxe de Analyze

```python
func.murmur_hash3_32(<expr>[, ...])
```

## Exemplos de Analyze

```python
func.murmur_hash3_32('hello')

┌───────────┐
│ 613153351  │
└───────────┘
```

## Sintaxe SQL

```sql
MURMUR_HASH3_32(<expr>[, ...])
```

## Exemplos SQL

```sql
SELECT MURMUR_HASH3_32('hello');

┌───────────┐
│ 613153351  │
└───────────┘
```
