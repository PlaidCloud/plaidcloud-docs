---
title: TRY_INET_ATON (Lakehouse v1)
description: TRY_INET_ATON — konwertuje adres IPv4 (ciąg w notacji z kropkami) na jego 32-bitową reprezentację całkowitoliczbową.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-aton.md
---

Funkcja try_inet_aton przyjmuje adres IPv4 zapisany jako ciąg znaków w notacji dziesiętnej z kropkami i zwraca wartość liczbową tego adresu IP w postaci liczby całkowitej.

## Składnia Analyze

```python
func.try_inet_aton(<str>)
```

## Przykłady Analyze

```python
func.try_inet_aton('10.0.5.9')

┌────────────────────────────────┐
│ func.try_inet_aton('10.0.5.9') │
├────────────────────────────────┤
│                      167773449 │
└────────────────────────────────┘
```

## Składnia SQL

```sql
TRY_INET_ATON( <str> )
```

## Aliasy

- [TRY_IPV4_STRING_TO_NUM](../try-ipv4-string-to-num)

## Zwracany typ

Liczba całkowita.

## Przykłady SQL

```sql
SELECT TRY_INET_ATON('10.0.5.9'), TRY_IPV4_STRING_TO_NUM('10.0.5.9');

┌────────────────────────────────────────────────────────────────┐
│ try_inet_aton('10.0.5.9') │ try_ipv4_string_to_num('10.0.5.9') │
│           UInt32          │               UInt32               │
├───────────────────────────┼────────────────────────────────────┤
│                 167773449 │                          167773449 │
└────────────────────────────────────────────────────────────────┘
```
