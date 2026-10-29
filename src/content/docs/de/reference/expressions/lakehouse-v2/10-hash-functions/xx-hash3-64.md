---
title: XX_HASH3_64 (Lakehouse v2)
description: XX_HASH3_64 – gibt den 64-Bit-xxHash3-Hash eines Werts zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/10-hash-functions/xx-hash3-64.md
---

Gibt den 64-Bit-xxHash3-Hash eines Werts zurück.

## Analyze-Syntax

```python
func.xx_hash3_64(<expr>[, ...])
```

## Analyze-Beispiele

```python
func.xx_hash3_64('hello')

┌──────────┐
│ (bigint)  │
└──────────┘
```

## SQL-Syntax

```sql
XX_HASH3_64(<expr>[, ...])
```

## SQL-Beispiele

```sql
SELECT XX_HASH3_64('hello');

┌──────────────────────┐
│ -7685981735718036227  │
└──────────────────────┘
```
