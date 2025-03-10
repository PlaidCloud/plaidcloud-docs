---
title: MD5
---

Calculates an MD5 128-bit checksum for a string. The value is returned as a string of 32 hexadecimal digits or NULL if the argument was NULL.

## Analyze Syntax

```python
func.md5(<expr>)
```

## Analyze Examples

```python
func.md5('1234567890')

+------------------------------------------+
| func.md5('1234567890')                   |
+------------------------------------------+
| e807f1fcf82d132f9bb018ca6738a19f         |
+------------------------------------------+
```

## SQL Syntax

```sql
MD5(<expr>)
```

## SQL Examples

```sql
SELECT MD5('1234567890');

┌──────────────────────────────────┐
│         md5('1234567890')        │
├──────────────────────────────────┤
│ e807f1fcf82d132f9bb018ca6738a19f │
└──────────────────────────────────┘
```