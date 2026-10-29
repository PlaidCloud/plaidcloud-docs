---
title: MD5SUM_NUMERIC (Lakehouse v2)
description: MD5SUM_NUMERIC – gibt den MD5-Hash mehrerer Zeichenfolgen als numerischen 128-Bit-Wert zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum-numeric.md
---

Gibt den MD5-Hash mehrerer Zeichenfolgen als numerischen 128-Bit-Wert zurück.

## Analyze-Syntax

```python
func.md5sum_numeric(<str1>[, <str2>, ...])
```

## Analyze-Beispiele

```python
func.md5sum_numeric('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQL-Syntax

```sql
MD5SUM_NUMERIC(<str1>[, <str2>, ...])
```

## SQL-Beispiele

```sql
SELECT MD5SUM_NUMERIC('hello');

┌─────────────────────────────────────────┐
│ 268224579284945131320661290344218476706  │
└─────────────────────────────────────────┘
```
