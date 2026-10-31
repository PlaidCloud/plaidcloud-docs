---
title: SIPHASH64 (Lakehouse v1)
description: SIPHASH64 erzeugt einen 64-Bit-SipHash-Hash-Wert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/siphash64.md
---

Erzeugt einen 64-Bit-[SipHash](https://en.wikipedia.org/wiki/SipHash)-Hash-Wert.

## Analyze-Syntax

```python
func.siphash64(<expr>)
```

## Analyze-Beispiele

```python
func.siphash64('1234567890')

┌───────────────────────────────┐
│ func.siphash64('1234567890')  │
├───────────────────────────────┤
│          18110648197875983073 │
└───────────────────────────────┘
```

## SQL-Syntax

```sql
SIPHASH64(<expr>)
```

## Aliasse

- [SIPHASH](../siphash)

## SQL-Beispiele

```sql
SELECT SIPHASH('1234567890'), SIPHASH64('1234567890');

┌─────────────────────────────────────────────────┐
│ siphash('1234567890') │ siphash64('1234567890') │
├───────────────────────┼─────────────────────────┤
│  18110648197875983073 │    18110648197875983073 │
└─────────────────────────────────────────────────┘
```
