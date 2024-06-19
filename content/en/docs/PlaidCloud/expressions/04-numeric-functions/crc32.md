---
title: CRC32
---

Returns the CRC32 checksum of `x`, where 'x' is expected to be a string and (if possible) is treated as one if it is not.

## Analyze Syntax

```python
func.crc32( '<x>' )
```

## Analyze Examples

```python
func.crc32('databend')

┌────────────────────────┐
│ func.crc32('databend') │
├────────────────────────┤
│             1177678456 │
└────────────────────────┘
```

## SQL Syntax

```sql
CRC32( '<x>' )
```

## SQL Examples

```sql
SELECT CRC32('databend');

┌───────────────────┐
│ crc32('databend') │
├───────────────────┤
│        1177678456 │
└───────────────────┘
```