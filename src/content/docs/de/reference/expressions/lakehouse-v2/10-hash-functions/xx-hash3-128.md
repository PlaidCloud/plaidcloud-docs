---
title: XX_HASH3_128 (Lakehouse v2)
description: XX_HASH3_128 – gibt den 128-Bit-xxHash3-Hash eines Werts zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-128.md
---

Gibt den 128-Bit-xxHash3-Hash eines Werts zurück.

## Analyze-Syntax

```python
func.xx_hash3_128(<expr>[, ...])
```

## Analyze-Beispiele

```python
func.xx_hash3_128('hello')

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQL-Syntax

```sql
XX_HASH3_128(<expr>[, ...])
```

## SQL-Beispiele

```sql
SELECT XX_HASH3_128('hello');

┌──────────────────────┐
│ (128-bit hash value)  │
└──────────────────────┘
```
