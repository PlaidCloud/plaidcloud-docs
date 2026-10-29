---
title: CITY64WITHSEED (Lakehouse v1)
description: CITY64WITHSEED berechnet einen 64-Bit-City64WithSeed-Hash für eine Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/city64withseed.md
---

Berechnet einen 64-Bit-City64WithSeed-Hash für eine Zeichenfolge.

## Analyze-Syntax

```python
func.city64withseed(<expr1>, <expr2>)
```

## Analyze-Beispiele

```python
func.city64withseed('1234567890', 12)

┌───────────────────────────────────────┐
│ func.city64withseed('1234567890', 12) │
├───────────────────────────────────────┤
│                  10660895976650300430 │
└───────────────────────────────────────┘
```

## SQL-Syntax

```sql
CITY64WITHSEED(<expr1>, <expr2>)
```

## SQL-Beispiele

```sql
SELECT CITY64WITHSEED('1234567890', 12);

┌──────────────────────────────────┐
│ city64withseed('1234567890', 12) │
├──────────────────────────────────┤
│             10660895976650300430 │
└──────────────────────────────────┘
```
