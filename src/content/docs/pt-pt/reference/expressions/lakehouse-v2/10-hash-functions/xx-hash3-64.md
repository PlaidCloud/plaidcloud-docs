---
title: XX_HASH3_64 (Lakehouse v2)
description: XX_HASH3_64 — devolve o hash xxHash3 de 64 bits de um valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-64.md
---

Devolve o hash xxHash3 de 64 bits de um valor.

## Sintaxe de Analyze

```python
func.xx_hash3_64(<expr>[, ...])
```

## Exemplos de Analyze

```python
func.xx_hash3_64('hello')

┌──────────┐
│ (bigint)  │
└──────────┘
```

## Sintaxe SQL

```sql
XX_HASH3_64(<expr>[, ...])
```

## Exemplos SQL

```sql
SELECT XX_HASH3_64('hello');

┌──────────────────────┐
│ -7685981735718036227  │
└──────────────────────┘
```
