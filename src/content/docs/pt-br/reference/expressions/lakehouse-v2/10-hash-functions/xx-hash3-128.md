---
title: XX_HASH3_128 (Lakehouse v2)
description: XX_HASH3_128 — retorna o hash xxHash3 de 128 bits de um valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-128.md
---

Retorna o hash xxHash3 de 128 bits de um valor.

## Sintaxe do Analyze

```python
func.xx_hash3_128(<expr>[, ...])
```

## Exemplos do Analyze

```python
func.xx_hash3_128('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## Sintaxe SQL

```sql
XX_HASH3_128(<expr>[, ...])
```

## Exemplos de SQL

```sql
SELECT XX_HASH3_128('hello');

┌──────────────────────┐
│ (128-bit hash value)  │
└──────────────────────┘
```
