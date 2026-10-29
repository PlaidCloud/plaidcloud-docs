---
title: CITY64WITHSEED (Lakehouse v1)
description: CITY64WITHSEED — oblicza 64-bitowy skrót City64WithSeed dla ciągu znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/city64withseed.md
---

Oblicza 64-bitowy skrót City64WithSeed dla ciągu znaków.

## Składnia Analyze

```python
func.city64withseed(<expr1>, <expr2>)
```

## Przykłady Analyze

```python
func.city64withseed('1234567890', 12)

┌───────────────────────────────────────┐
│ func.city64withseed('1234567890', 12) │
├───────────────────────────────────────┤
│                  10660895976650300430 │
└───────────────────────────────────────┘
```

## Składnia SQL

```sql
CITY64WITHSEED(<expr1>, <expr2>)
```

## Przykłady SQL

```sql
SELECT CITY64WITHSEED('1234567890', 12);

┌──────────────────────────────────┐
│ city64withseed('1234567890', 12) │
├──────────────────────────────────┤
│             10660895976650300430 │
└──────────────────────────────────┘
```
