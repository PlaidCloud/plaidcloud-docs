---
title: SIPHASH64 (Lakehouse v1)
description: SIPHASH64 produce un valor hash SipHash de 64 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/siphash64.md
---

Produce un valor hash [SipHash](https://en.wikipedia.org/wiki/SipHash) de 64 bits.

## Sintaxis de Analyze

```python
func.siphash64(<expr>)
```

## Ejemplos de Analyze

```python
func.siphash64('1234567890')

┌───────────────────────────────┐
│ func.siphash64('1234567890')  │
├───────────────────────────────┤
│          18110648197875983073 │
└───────────────────────────────┘
```

## Sintaxis de SQL

```sql
SIPHASH64(<expr>)
```

## Alias

- [SIPHASH](../siphash)

## Ejemplos de SQL

```sql
SELECT SIPHASH('1234567890'), SIPHASH64('1234567890');

┌─────────────────────────────────────────────────┐
│ siphash('1234567890') │ siphash64('1234567890') │
├───────────────────────┼─────────────────────────┤
│  18110648197875983073 │    18110648197875983073 │
└─────────────────────────────────────────────────┘
```
