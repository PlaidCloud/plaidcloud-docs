---
title: INET_NTOA (Lakehouse v1)
description: INET_NTOA — converte um número inteiro de 32 bits num endereço IPv4.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/inet-ntoa.md
---

Converte um número inteiro de 32 bits num endereço IPv4.

## Sintaxe do Analyze

```python
func.inet_ntoa(<int32>)
```

## Exemplos do Analyze

```python
SELECT func.inet_ntoa(16909060)

┌──────────────────────────────┐
│ func.inet_ntoa(16909060)     │
├──────────────────────────────┤
│ 1.2.3.4                      │
└──────────────────────────────┘
```

## Sintaxe SQL

```sql
INET_NOTA( <int32> )
```

## Aliases

- [IPV4_NUM_TO_STRING](../ipv4-num-to-string)

## Tipo de retorno

Cadeia de caracteres.

## Exemplos de SQL

```sql
SELECT IPV4_NUM_TO_STRING(16909060), INET_NTOA(16909060);

┌────────────────────────────────────────────────────┐
│ ipv4_num_to_string(16909060) │ inet_ntoa(16909060) │
├──────────────────────────────┼─────────────────────┤
│ 1.2.3.4                      │ 1.2.3.4             │
└────────────────────────────────────────────────────┘
```
