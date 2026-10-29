---
title: MD5 (Lakehouse v1)
description: MD5 — oblicza 128-bitową sumę kontrolną MD5 dla ciągu znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/md5.md
---

Oblicza 128-bitową sumę kontrolną MD5 dla ciągu znaków. Wartość jest zwracana jako ciąg 32 cyfr szesnastkowych lub NULL, jeśli argument miał wartość NULL.

## Składnia Analyze

```python
func.md5(<expr>)
```

## Przykłady Analyze

```python
func.md5('1234567890')

┌──────────────────────────────────────────┐
│ func.md5('1234567890')                   │
├──────────────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f         │
└──────────────────────────────────────────┘
```

## Składnia SQL

```sql
MD5(<expr>)
```

## Przykłady SQL

```sql
SELECT MD5('1234567890');

┌──────────────────────────────────┐
│         md5('1234567890')        │
├──────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f │
└──────────────────────────────────┘
```
