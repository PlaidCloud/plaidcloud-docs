---
title: MD5SUM_NUMERIC (Lakehouse v2)
description: MD5SUM_NUMERIC — retorna o hash MD5 de várias strings como um valor numérico de 128 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum-numeric.md
---

Retorna o hash MD5 de várias strings como um valor numérico de 128 bits.

## Sintaxe do Analyze

```python
func.md5sum_numeric(<str1>[, <str2>, ...])
```

## Exemplos do Analyze

```python
func.md5sum_numeric('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## Sintaxe SQL

```sql
MD5SUM_NUMERIC(<str1>[, <str2>, ...])
```

## Exemplos SQL

```sql
SELECT MD5SUM_NUMERIC('hello');

┌─────────────────────────────────────────┐
│ 268224579284945131320661290344218476706  │
└─────────────────────────────────────────┘
```
