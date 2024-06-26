---
title: TRY_INET_NTOA
---

Takes an IPv4 address in network byte order and then returns the address as a dotted-quad string representation.

## Analyze Syntax

```python
func.try_inet_ntoa(<integer>)
```

## Analyze Examples

```python
func.try_inet_ntoaA(167773449)

┌───────────────────────────────┐
│ func.try_inet_ntoa(167773449) │
├───────────────────────────────┤
│ 10.0.5.9                      │
└───────────────────────────────┘
```

## SQL Syntax

```sql
TRY_INET_NTOA( <integer> )
```

## Aliases

- [TRY_IPV4_NUM_TO_STRING](../try-ipv4-num-to-string)

## Return Type

String.

## SQL Examples

```sql
SELECT TRY_INET_NTOA(167773449), TRY_IPV4_NUM_TO_STRING(167773449);

┌──────────────────────────────────────────────────────────────┐
│ try_inet_ntoa(167773449) │ try_ipv4_num_to_string(167773449) │
├──────────────────────────┼───────────────────────────────────┤
│ 10.0.5.9                 │ 10.0.5.9                          │
└──────────────────────────────────────────────────────────────┘
```