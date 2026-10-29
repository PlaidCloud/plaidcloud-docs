---
title: SIPHASH64 (Lakehouse v1)
description: SIPHASH64 — produit une valeur de hachage SipHash de 64 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/siphash64.md
---

Produit une valeur de hachage [SipHash](https://en.wikipedia.org/wiki/SipHash) de 64 bits.

## Syntaxe Analyze

```python
func.siphash64(<expr>)
```

## Exemples Analyze

```python
func.siphash64('1234567890')

┌───────────────────────────────┐
│ func.siphash64('1234567890')  │
├───────────────────────────────┤
│          18110648197875983073 │
└───────────────────────────────┘
```

## Syntaxe SQL

```sql
SIPHASH64(<expr>)
```

## Alias

- [SIPHASH](../siphash)

## Exemples SQL

```sql
SELECT SIPHASH('1234567890'), SIPHASH64('1234567890');

┌─────────────────────────────────────────────────┐
│ siphash('1234567890') │ siphash64('1234567890') │
├───────────────────────┼─────────────────────────┤
│  18110648197875983073 │    18110648197875983073 │
└─────────────────────────────────────────────────┘
```
