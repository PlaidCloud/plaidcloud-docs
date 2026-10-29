---
title: SIPHASH64 (Lakehouse v1)
description: SIPHASH64 — produz um valor de hash SipHash de 64 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/siphash64.md
---

Produz um valor de hash [SipHash](https://en.wikipedia.org/wiki/SipHash) de 64 bits.

## Sintaxe do Analyze

```python
func.siphash64(<expr>)
```

## Exemplos do Analyze

```python
func.siphash64('1234567890')

┌───────────────────────────────┐
│ func.siphash64('1234567890')  │
├───────────────────────────────┤
│          18110648197875983073 │
└───────────────────────────────┘
```

## Sintaxe SQL

```sql
SIPHASH64(<expr>)
```

## Aliases

- [SIPHASH](../siphash)

## Exemplos de SQL

```sql
SELECT SIPHASH('1234567890'), SIPHASH64('1234567890');

┌─────────────────────────────────────────────────┐
│ siphash('1234567890') │ siphash64('1234567890') │
├───────────────────────┼─────────────────────────┤
│  18110648197875983073 │    18110648197875983073 │
└─────────────────────────────────────────────────┘
```
