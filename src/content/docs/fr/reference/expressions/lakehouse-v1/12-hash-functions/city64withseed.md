---
title: CITY64WITHSEED (Lakehouse v1)
description: CITY64WITHSEED — calcule un hachage City64WithSeed de 64 bits pour une chaîne.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/city64withseed.md
---

Calcule un hachage City64WithSeed de 64 bits pour une chaîne.

## Syntaxe Analyze

```python
func.city64withseed(<expr1>, <expr2>)
```

## Exemples Analyze

```python
func.city64withseed('1234567890', 12)

┌───────────────────────────────────────┐
│ func.city64withseed('1234567890', 12) │
├───────────────────────────────────────┤
│                  10660895976650300430 │
└───────────────────────────────────────┘
```

## Syntaxe SQL

```sql
CITY64WITHSEED(<expr1>, <expr2>)
```

## Exemples SQL

```sql
SELECT CITY64WITHSEED('1234567890', 12);

┌──────────────────────────────────┐
│ city64withseed('1234567890', 12) │
├──────────────────────────────────┤
│             10660895976650300430 │
└──────────────────────────────────┘
```
