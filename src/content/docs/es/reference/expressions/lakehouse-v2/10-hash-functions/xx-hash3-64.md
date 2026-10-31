---
title: XX_HASH3_64 (Lakehouse v2)
description: XX_HASH3_64 — devuelve el hash xxHash3 de 64 bits de un valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-64.md
---

Devuelve el hash xxHash3 de 64 bits de un valor.

## Sintaxis de Analyze

```python
func.xx_hash3_64(<expr>[, ...])
```

## Ejemplos de Analyze

```python
func.xx_hash3_64('hello')

┌──────────┐
│ (bigint)  │
└──────────┘
```

## Sintaxis de SQL

```sql
XX_HASH3_64(<expr>[, ...])
```

## Ejemplos de SQL

```sql
SELECT XX_HASH3_64('hello');

┌──────────────────────┐
│ -7685981735718036227  │
└──────────────────────┘
```
