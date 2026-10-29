---
title: XX_HASH3_128 (Lakehouse v2)
description: XX_HASH3_128 — devuelve el hash xxHash3 de 128 bits de un valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-128.md
---

Devuelve el hash xxHash3 de 128 bits de un valor.

## Sintaxis de Analyze

```python
func.xx_hash3_128(<expr>[, ...])
```

## Ejemplos de Analyze

```python
func.xx_hash3_128('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## Sintaxis de SQL

```sql
XX_HASH3_128(<expr>[, ...])
```

## Ejemplos de SQL

```sql
SELECT XX_HASH3_128('hello');

┌──────────────────────┐
│ (128-bit hash value)  │
└──────────────────────┘
```
