---
title: SM3 (Lakehouse v2)
description: SM3 — zwraca skrót SM3 ciągu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sm3.md
---

Zwraca skrót SM3 ciągu.

## Składnia Analyze

```python
func.sm3(<str>)
```

## Przykłady Analyze

```python
func.sm3('hello')

┌───────────────┐
│ 'becbbfaa...'  │
└───────────────┘
```

## Składnia SQL

```sql
SM3(<str>)
```

## Przykłady SQL

```sql
SELECT SM3('hello');

┌──────────────────────────────────────────────────────────────────┐
│ becbbfaae6548b8bf0cfcad5a27183cd1be6093b1cceccc303d9c61d0a645268  │
└──────────────────────────────────────────────────────────────────┘
```
