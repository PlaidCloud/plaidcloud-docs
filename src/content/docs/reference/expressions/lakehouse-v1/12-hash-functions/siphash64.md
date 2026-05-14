---
title: SIPHASH64
description: "Learn how to use the SIPHASH64 hash function in PlaidCloud Lakehouse. Produces a 64-bit SipHash hash value. Full syntax and usage reference."
---

Produces a 64-bit [SipHash](https://en.wikipedia.org/wiki/SipHash) hash value.

## Analyze Syntax

```python
func.siphash64(<expr>)
```

## Analyze Examples

```python
func.siphash64('1234567890')

┌───────────────────────────────┐
│ func.siphash64('1234567890')  │
├───────────────────────────────┤
│          18110648197875983073 │
└───────────────────────────────┘
```

## SQL Syntax

```sql
SIPHASH64(<expr>)
```

## Aliases

- [SIPHASH](../siphash)

## SQL Examples

```sql
SELECT SIPHASH('1234567890'), SIPHASH64('1234567890');

┌─────────────────────────────────────────────────┐
│ siphash('1234567890') │ siphash64('1234567890') │
├───────────────────────┼─────────────────────────┤
│  18110648197875983073 │    18110648197875983073 │
└─────────────────────────────────────────────────┘
```
