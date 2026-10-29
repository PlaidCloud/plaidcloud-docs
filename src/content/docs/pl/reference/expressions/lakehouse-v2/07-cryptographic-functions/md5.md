---
title: MD5 (Lakehouse v2)
description: MD5 — zwraca skrót MD5 ciągu jako 32-znakowy ciąg szesnastkowy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5.md
---

Zwraca skrót MD5 ciągu jako 32-znakowy ciąg szesnastkowy.

## Składnia Analyze

```python
func.md5(<str>)
```

## Przykłady Analyze

```python
func.md5('hello')

┌────────────────────────────────────┐
│ '5d41402abc4b2a76b9719d911017c592'  │
└────────────────────────────────────┘
```

## Składnia SQL

```sql
MD5(<str>)
```

## Przykłady SQL

```sql
SELECT MD5('hello');

┌──────────────────────────────────┐
│ 5d41402abc4b2a76b9719d911017c592  │
└──────────────────────────────────┘
```
