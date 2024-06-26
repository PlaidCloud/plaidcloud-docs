---
title: TRY_INET_ATON
---

try_inet_aton function is used to take the dotted-quad representation of an IPv4 address as a string and returns the numeric value of the given IP address in form of an integer.

## Analyze Syntax

```python
func.try_inet_aton(<str>)
```

## Analyze Examples

```python
func.try_inet_aton('10.0.5.9')

┌────────────────────────────────┐
│ func.try_inet_aton('10.0.5.9') │
├────────────────────────────────┤
│                      167773449 │
└────────────────────────────────┘
```

## SQL Syntax

```sql
TRY_INET_ATON( <str> )
```

## Aliases

- [TRY_IPV4_STRING_TO_NUM](../try-ipv4-string-to-num)

## Return Type

Integer.

## SQL Examples

```sql
SELECT TRY_INET_ATON('10.0.5.9'), TRY_IPV4_STRING_TO_NUM('10.0.5.9');

┌────────────────────────────────────────────────────────────────┐
│ try_inet_aton('10.0.5.9') │ try_ipv4_string_to_num('10.0.5.9') │
│           UInt32          │               UInt32               │
├───────────────────────────┼────────────────────────────────────┤
│                 167773449 │                          167773449 │
└────────────────────────────────────────────────────────────────┘
```