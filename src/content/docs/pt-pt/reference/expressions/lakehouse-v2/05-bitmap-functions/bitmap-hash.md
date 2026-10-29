---
title: BITMAP_HASH (Lakehouse v2)
description: BITMAP_HASH — calcula um hash de 32 bits de um valor e devolve um bitmap que contém esse hash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-hash.md
---

Calcula um hash de 32 bits de um valor e devolve um bitmap que contém esse hash.

## Sintaxe do Analyze

```python
func.bitmap_hash(<value>)
```

## Exemplos do Analyze

```python
func.bitmap_hash('hello')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP_HASH(<value>)
```

## Exemplos SQL

```sql
SELECT BITMAP_COUNT(BITMAP_HASH('hello'));

┌───┐
│ 1 │
└───┘
```
