---
title: SHA2 (Lakehouse v2)
description: SHA2 — zwraca skrót SHA-2 ciągu dla podanej długości w bitach (224, 256, 384 lub 512).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sha2.md
---

Zwraca skrót SHA-2 ciągu dla podanej długości w bitach (224, 256, 384 lub 512).

## Składnia Analyze

```python
func.sha2(<str>, <bit_length>)
```

## Przykłady Analyze

```python
func.sha2('hello', 256)

┌───────────────┐
│ '2cf24dba...'  │
└───────────────┘
```

## Składnia SQL

```sql
SHA2(<str>, <bit_length>)
```

## Przykłady SQL

```sql
SELECT SHA2('hello', 256);

┌──────────────────────────────────────────────────────────────────┐
│ 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824  │
└──────────────────────────────────────────────────────────────────┘
```
