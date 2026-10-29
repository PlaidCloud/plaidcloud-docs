---
title: INET_ATON (Lakehouse v1)
description: INET_ATON — konwertuje adres IPv4 na 32-bitową liczbę całkowitą.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/inet-aton.md
---

Konwertuje adres IPv4 na 32-bitową liczbę całkowitą.

## Składnia Analyze

```python
func.inet_aton(<ip>)
```

## Przykłady Analyze

```python
func.inet_aton('1.2.3.4')

┌───────────────────────────────┐
│ func.inet_aton('1.2.3.4')     │
├───────────────────────────────┤
│                      16909060 │
└───────────────────────────────┘
```

## Składnia SQL

```sql
INET_ATON(<ip>)
```

## Aliasy

- [IPV4_STRING_TO_NUM](../ipv4-string-to-num)

## Zwracany typ

Liczba całkowita.

## Przykłady SQL

```sql
SELECT IPV4_STRING_TO_NUM('1.2.3.4'), INET_ATON('1.2.3.4');

┌──────────────────────────────────────────────────────┐
│ ipv4_string_to_num('1.2.3.4') │ inet_aton('1.2.3.4') │
├───────────────────────────────┼──────────────────────┤
│                      16909060 │             16909060 │
└──────────────────────────────────────────────────────┘
```
