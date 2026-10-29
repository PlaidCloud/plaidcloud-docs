---
title: XXHASH32 (Lakehouse v1)
description: XXHASH32 berechnet einen 32-Bit-xxHash32-Hash-Wert für eine Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/xxhash32.md
---

Berechnet einen 32-Bit-xxHash32-Hash-Wert für eine Zeichenfolge. Der Wert wird als UInt32 zurückgegeben oder als NULL, wenn das Argument NULL war.

## Analyze-Syntax

```python
func.xxhash32(<expr>)
```

## Analyze-Beispiele

```python
func.xxhash32('1234567890')

┌─────────────────────────────┐
│ func.xxhash32('1234567890') │
├─────────────────────────────┤
│                  3896585587 │
└─────────────────────────────┘
```

## SQL-Syntax

```sql
XXHASH32(<expr>)
```

## SQL-Beispiele

```sql
SELECT XXHASH32('1234567890');

┌────────────────────────┐
│ xxhash32('1234567890') │
├────────────────────────┤
│             3896585587 │
└────────────────────────┘
```
