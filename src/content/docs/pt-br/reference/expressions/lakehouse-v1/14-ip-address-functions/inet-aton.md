---
title: INET_ATON (Lakehouse v1)
description: INET_ATON — converte um endereço IPv4 em um inteiro de 32 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/inet-aton.md
---

Converte um endereço IPv4 em um inteiro de 32 bits.

## Sintaxe no Analyze

```python
func.inet_aton(<ip>)
```

## Exemplos no Analyze

```python
func.inet_aton('1.2.3.4')

┌───────────────────────────────┐
│ func.inet_aton('1.2.3.4')     │
├───────────────────────────────┤
│                      16909060 │
└───────────────────────────────┘
```

## Sintaxe SQL

```sql
INET_ATON(<ip>)
```

## Aliases

- [IPV4_STRING_TO_NUM](../ipv4-string-to-num)

## Tipo de retorno

Inteiro.

## Exemplos de SQL

```sql
SELECT IPV4_STRING_TO_NUM('1.2.3.4'), INET_ATON('1.2.3.4');

┌──────────────────────────────────────────────────────┐
│ ipv4_string_to_num('1.2.3.4') │ inet_aton('1.2.3.4') │
├───────────────────────────────┼──────────────────────┤
│                      16909060 │             16909060 │
└──────────────────────────────────────────────────────┘
```
