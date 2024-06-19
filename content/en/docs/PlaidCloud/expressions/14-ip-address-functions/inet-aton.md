---
title: INET_ATON
---

Converts an IPv4 address to a 32-bit integer.

## Analyze Syntax

```python
func.inet_aton(<ip>)
```

## Analyze Examples

```python
func.inet_aton('1.2.3.4')

┌───────────────────────────────┐
│ func.inet_aton('1.2.3.4')     │
├───────────────────────────────┤
│                      16909060 │
└───────────────────────────────┘
```

## SQL Syntax

```sql
INET_ATON(<ip>)
```

## Aliases

- [IPV4_STRING_TO_NUM](../ipv4-string-to-num)

## Return Type

Integer.

## SQL Examples

```sql
SELECT IPV4_STRING_TO_NUM('1.2.3.4'), INET_ATON('1.2.3.4');

┌──────────────────────────────────────────────────────┐
│ ipv4_string_to_num('1.2.3.4') │ inet_aton('1.2.3.4') │
├───────────────────────────────┼──────────────────────┤
│                      16909060 │             16909060 │
└──────────────────────────────────────────────────────┘
```