---
title: MD5SUM_NUMERIC (Lakehouse v2)
description: MD5SUM_NUMERIC — devuelve el hash MD5 de varias cadenas como un valor numérico de 128 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum-numeric.md
---

Devuelve el hash MD5 de varias cadenas como un valor numérico de 128 bits.

## Sintaxis de Analyze

```python
func.md5sum_numeric(<str1>[, <str2>, ...])
```

## Ejemplos de Analyze

```python
func.md5sum_numeric('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## Sintaxis de SQL

```sql
MD5SUM_NUMERIC(<str1>[, <str2>, ...])
```

## Ejemplos de SQL

```sql
SELECT MD5SUM_NUMERIC('hello');

┌─────────────────────────────────────────┐
│ 268224579284945131320661290344218476706  │
└─────────────────────────────────────────┘
```
