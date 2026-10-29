---
title: TRY_INET_ATON (Lakehouse v1)
description: TRY_INET_ATON convierte una dirección IPv4 (cadena con notación de cuatro puntos) en su representación como entero de 32 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-aton.md
---

La función try_inet_aton toma la representación con notación de cuatro puntos de una dirección IPv4 como cadena y devuelve el valor numérico de la dirección IP dada en forma de entero.

## Sintaxis de Analyze

```python
func.try_inet_aton(<str>)
```

## Ejemplos de Analyze

```python
func.try_inet_aton('10.0.5.9')

┌────────────────────────────────┐
│ func.try_inet_aton('10.0.5.9') │
├────────────────────────────────┤
│                      167773449 │
└────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TRY_INET_ATON( <str> )
```

## Alias

- [TRY_IPV4_STRING_TO_NUM](../try-ipv4-string-to-num)

## Tipo de retorno

Entero.

## Ejemplos de SQL

```sql
SELECT TRY_INET_ATON('10.0.5.9'), TRY_IPV4_STRING_TO_NUM('10.0.5.9');

┌────────────────────────────────────────────────────────────────┐
│ try_inet_aton('10.0.5.9') │ try_ipv4_string_to_num('10.0.5.9') │
│           UInt32          │               UInt32               │
├───────────────────────────┼────────────────────────────────────┤
│                 167773449 │                          167773449 │
└────────────────────────────────────────────────────────────────┘
```
