---
title: CRC32 (Lakehouse v2)
description: CRC32 — Gibt die CRC-32-Prüfsumme einer Zeichenfolge als vorzeichenlose Ganzzahl zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/crc32.md
---

Gibt die CRC-32-Prüfsumme einer Zeichenfolge als vorzeichenlose Ganzzahl zurück.

## Analyze-Syntax

```python
func.crc32(<str>)
```

## Analyze-Beispiele

```python
func.crc32('hello')

┌───────────┐
│ 907060870  │
└───────────┘
```

## SQL-Syntax

```sql
CRC32(<str>)
```

## SQL-Beispiele

```sql
SELECT CRC32('hello');

┌───────────┐
│ 907060870  │
└───────────┘
```
