---
title: MD5SUM_NUMERIC (Lakehouse v2)
description: MD5SUM_NUMERIC — zwraca skrót MD5 wielu ciągów jako 128-bitową wartość liczbową.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum-numeric.md
---

Zwraca skrót MD5 wielu ciągów jako 128-bitową wartość liczbową.

## Składnia Analyze

```python
func.md5sum_numeric(<str1>[, <str2>, ...])
```

## Przykłady Analyze

```python
func.md5sum_numeric('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## Składnia SQL

```sql
MD5SUM_NUMERIC(<str1>[, <str2>, ...])
```

## Przykłady SQL

```sql
SELECT MD5SUM_NUMERIC('hello');

┌─────────────────────────────────────────┐
│ 268224579284945131320661290344218476706  │
└─────────────────────────────────────────┘
```
