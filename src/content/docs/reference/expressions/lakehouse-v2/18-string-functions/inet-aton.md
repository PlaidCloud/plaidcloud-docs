---
title: INET_ATON (Lakehouse v2)
description: INET_ATON — Converts an IPv4 address string to a numeric value.
---

Converts an IPv4 address string to a numeric value.

## Analyze Syntax

```python
func.inet_aton(<ip_str>)
```

## Analyze Examples

```python
func.inet_aton('192.168.1.1')

┌────────────┐
│ 3232235777  │
└────────────┘
```

## SQL Syntax

```sql
INET_ATON(<ip_str>)
```

## SQL Examples

```sql
SELECT INET_ATON('192.168.1.1');

┌────────────┐
│ 3232235777  │
└────────────┘
```
