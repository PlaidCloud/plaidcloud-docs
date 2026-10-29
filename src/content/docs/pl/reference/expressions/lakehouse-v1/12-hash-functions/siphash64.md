---
title: SIPHASH64 (Lakehouse v1)
description: SIPHASH64 — zwraca 64-bitową wartość skrótu SipHash.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/siphash64.md
---

Zwraca 64-bitową wartość skrótu [SipHash](https://en.wikipedia.org/wiki/SipHash).

## Składnia Analyze

```python
func.siphash64(<expr>)
```

## Przykłady Analyze

```python
func.siphash64('1234567890')

┌───────────────────────────────┐
│ func.siphash64('1234567890')  │
├───────────────────────────────┤
│          18110648197875983073 │
└───────────────────────────────┘
```

## Składnia SQL

```sql
SIPHASH64(<expr>)
```

## Aliasy

- [SIPHASH](../siphash)

## Przykłady SQL

```sql
SELECT SIPHASH('1234567890'), SIPHASH64('1234567890');

┌─────────────────────────────────────────────────┐
│ siphash('1234567890') │ siphash64('1234567890') │
├───────────────────────┼─────────────────────────┤
│  18110648197875983073 │    18110648197875983073 │
└─────────────────────────────────────────────────┘
```
