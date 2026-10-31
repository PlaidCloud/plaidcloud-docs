---
title: TRY_INET_NTOA (Lakehouse v1)
description: TRY_INET_NTOA convierte una dirección IPv4 en orden de bytes de red en su representación como cadena con notación de cuatro puntos y devuelve NULL si falla.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-ntoa.md
---

Toma una dirección IPv4 en orden de bytes de red y devuelve la dirección como una cadena con notación de cuatro puntos.

## Sintaxis de Analyze

```python
func.try_inet_ntoa(<integer>)
```

## Ejemplos de Analyze

```python
func.try_inet_ntoaA(167773449)

┌───────────────────────────────┐
│ func.try_inet_ntoa(167773449) │
├───────────────────────────────┤
│ 10.0.5.9                      │
└───────────────────────────────┘
```

## Sintaxis de SQL

```sql
TRY_INET_NTOA( <integer> )
```

## Alias

- [TRY_IPV4_NUM_TO_STRING](../try-ipv4-num-to-string)

## Tipo de retorno

Cadena.

## Ejemplos de SQL

```sql
SELECT TRY_INET_NTOA(167773449), TRY_IPV4_NUM_TO_STRING(167773449);

┌──────────────────────────────────────────────────────────────┐
│ try_inet_ntoa(167773449) │ try_ipv4_num_to_string(167773449) │
├──────────────────────────┼───────────────────────────────────┤
│ 10.0.5.9                 │ 10.0.5.9                          │
└──────────────────────────────────────────────────────────────┘
```
