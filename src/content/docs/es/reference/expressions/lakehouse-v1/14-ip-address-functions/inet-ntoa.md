---
title: INET_NTOA (Lakehouse v1)
description: INET_NTOA convierte un entero de 32 bits en una dirección IPv4.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/inet-ntoa.md
---

Convierte un entero de 32 bits en una dirección IPv4.

## Sintaxis de Analyze

```python
func.inet_ntoa(<int32>)
```

## Ejemplos de Analyze

```python
SELECT func.inet_ntoa(16909060)

┌──────────────────────────────┐
│ func.inet_ntoa(16909060)     │
├──────────────────────────────┤
│ 1.2.3.4                      │
└──────────────────────────────┘
```

## Sintaxis de SQL

```sql
INET_NOTA( <int32> )
```

## Alias

- [IPV4_NUM_TO_STRING](../ipv4-num-to-string)

## Tipo de retorno

Cadena.

## Ejemplos de SQL

```sql
SELECT IPV4_NUM_TO_STRING(16909060), INET_NTOA(16909060);

┌────────────────────────────────────────────────────┐
│ ipv4_num_to_string(16909060) │ inet_ntoa(16909060) │
├──────────────────────────────┼─────────────────────┤
│ 1.2.3.4                      │ 1.2.3.4             │
└────────────────────────────────────────────────────┘
```
