---
title: CRC32 (Lakehouse v1)
description: CRC32 – gibt die CRC32-Prüfsumme von x zurück, wobei x eine Zeichenfolge sein soll und, falls möglich, als solche behandelt wird.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/crc32.md
---

Gibt die CRC32-Prüfsumme von `x` zurück, wobei 'x' eine Zeichenfolge sein soll und, falls möglich, als solche behandelt wird, wenn es keine ist.

## Analyze-Syntax

```python
func.crc32( '<x>' )
```

## Analyze-Beispiele

```python
func.crc32('databend')

┌────────────────────────┐
│ func.crc32('databend') │
├────────────────────────┤
│             1177678456 │
└────────────────────────┘
```

## SQL-Syntax

```sql
CRC32( '<x>' )
```

## SQL-Beispiele

```sql
SELECT CRC32('databend');

┌───────────────────┐
│ crc32('databend') │
├───────────────────┤
│        1177678456 │
└───────────────────┘
```
