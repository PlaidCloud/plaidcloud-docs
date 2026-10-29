---
title: SHA (Lakehouse v1)
description: SHA — oblicza 160-bitową sumę kontrolną SHA-1 dla ciągu znaków, zgodnie z opisem w RFC 3174 (Secure Hash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/sha.md
---

Oblicza 160-bitową sumę kontrolną SHA-1 dla ciągu znaków, zgodnie z opisem w RFC 3174 (Secure Hash Algorithm). Wartość jest zwracana jako ciąg 40 cyfr szesnastkowych lub NULL, jeśli argument miał wartość NULL.

## Składnia Analyze

```python
func.sha(<expr>)
```

## Przykłady Analyze

```python
func.sha('1234567890')

┌──────────────────────────────────────────┐
│ func.sha('1234567890')                   │
├──────────────────────────────────────────┤
│ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │
└──────────────────────────────────────────┘
```

## Składnia SQL

```sql
SHA(<expr>)
```

## Aliasy

- [SHA1](../sha1)

## Przykłady SQL

```sql
SELECT SHA('1234567890'), SHA1('1234567890');

┌─────────────────────────────────────────────────────────────────────────────────────┐
│             sha('1234567890')            │            sha1('1234567890')            │
├──────────────────────────────────────────┼──────────────────────────────────────────┤
│ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │ 01b307acba4f54f55aafc33bb06bbbf6ca803e9a │
└─────────────────────────────────────────────────────────────────────────────────────┘
```
