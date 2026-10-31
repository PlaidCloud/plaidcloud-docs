---
title: XXHASH64 (Lakehouse v1)
description: XXHASH64 berechnet einen 64-Bit-xxHash64-Hash-Wert für eine Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash64.md
---

Berechnet einen 64-Bit-xxHash64-Hash-Wert für eine Zeichenfolge. Der Wert wird als UInt64 zurückgegeben oder als NULL, wenn das Argument NULL war.

## Analyze-Syntax

```python
func.xxhash64(<expr>)
```

## Analyze-Beispiele

```python
func.xxhash64('1234567890')

┌─────────────────────────────┐
│ func.xxhash64('1234567890') │
├─────────────────────────────┤
│        12237639266330420150 │
└─────────────────────────────┘
```

## SQL-Syntax

```sql
XXHASH64(<expr>)
```

## SQL-Beispiele

```sql
SELECT XXHASH64('1234567890');

┌────────────────────────┐
│ xxhash64('1234567890') │
├────────────────────────┤
│   12237639266330420150 │
└────────────────────────┘
```
