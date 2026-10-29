---
title: BITMAP_HASH64 (Lakehouse v2)
description: BITMAP_HASH64 — calcula um hash de 64 bits de um valor e retorna um bitmap contendo esse hash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash64.md
---

Calcula um hash de 64 bits de um valor e retorna um bitmap contendo esse hash.

## Sintaxe do Analyze

```python
func.bitmap_hash64(<value>)
```

## Exemplos do Analyze

```python
func.bitmap_hash64('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP_HASH64(<value>)
```

## Exemplos SQL

```sql
SELECT BITMAP_COUNT(BITMAP_HASH64('hello'));

┌───┐
│ 1 │
└───┘
```
