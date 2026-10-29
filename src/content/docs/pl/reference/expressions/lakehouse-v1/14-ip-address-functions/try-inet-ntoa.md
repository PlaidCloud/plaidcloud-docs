---
title: TRY_INET_NTOA (Lakehouse v1)
description: TRY_INET_NTOA — konwertuje adres IPv4 w kolejności bajtów sieciowej na ciąg w notacji z kropkami, a w razie niepowodzenia zwraca NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-ntoa.md
---

Przyjmuje adres IPv4 w kolejności bajtów sieciowej i zwraca ten adres jako ciąg znaków w notacji dziesiętnej z kropkami.

## Składnia Analyze

```python
func.try_inet_ntoa(<integer>)
```

## Przykłady Analyze

```python
func.try_inet_ntoaA(167773449)

┌───────────────────────────────┐
│ func.try_inet_ntoa(167773449) │
├───────────────────────────────┤
│ 10.0.5.9                      │
└───────────────────────────────┘
```

## Składnia SQL

```sql
TRY_INET_NTOA( <integer> )
```

## Aliasy

- [TRY_IPV4_NUM_TO_STRING](../try-ipv4-num-to-string)

## Zwracany typ

Ciąg znaków.

## Przykłady SQL

```sql
SELECT TRY_INET_NTOA(167773449), TRY_IPV4_NUM_TO_STRING(167773449);

┌──────────────────────────────────────────────────────────────┐
│ try_inet_ntoa(167773449) │ try_ipv4_num_to_string(167773449) │
├──────────────────────────┼───────────────────────────────────┤
│ 10.0.5.9                 │ 10.0.5.9                          │
└──────────────────────────────────────────────────────────────┘
```
