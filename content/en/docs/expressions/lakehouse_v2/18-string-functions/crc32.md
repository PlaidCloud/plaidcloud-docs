---
title: CRC32
---

Returns the CRC-32 checksum of a string as an unsigned integer.

## Analyze Syntax

```python
func.crc32(<str>)
```

## Analyze Examples

```python
func.crc32('hello')

┌───────────┐
│ 907060870  │
└───────────┘
```

## SQL Syntax

```sql
CRC32(<str>)
```

## SQL Examples

```sql
SELECT CRC32('hello');

┌───────────┐
│ 907060870  │
└───────────┘
```
