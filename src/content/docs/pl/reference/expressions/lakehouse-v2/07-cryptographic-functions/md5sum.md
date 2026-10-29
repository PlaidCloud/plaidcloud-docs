---
title: MD5SUM (Lakehouse v2)
description: MD5SUM — zwraca skrót MD5 wielu połączonych ze sobą ciągów.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum.md
---

Zwraca skrót MD5 wielu połączonych ze sobą ciągów.

## Składnia Analyze

```python
func.md5sum(<str1>[, <str2>, ...])
```

## Przykłady Analyze

```python
func.md5sum('hello', 'world')

┌────────────────────────────────────┐
│ 'fc5e038d38a57032085441e7fe7010b0'  │
└────────────────────────────────────┘
```

## Składnia SQL

```sql
MD5SUM(<str1>[, <str2>, ...])
```

## Przykłady SQL

```sql
SELECT MD5SUM('hello', 'world');

┌──────────────────────────────────┐
│ fc5e038d38a57032085441e7fe7010b0  │
└──────────────────────────────────┘
```
