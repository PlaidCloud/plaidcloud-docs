---
title: TRY_INET_ATON (Lakehouse v1)
description: TRY_INET_ATON — converte um endereço IPv4 (string em notação decimal com pontos) em sua representação de inteiro de 32 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-aton.md
---

A função try_inet_aton recebe a representação decimal com pontos de um endereço IPv4 como string e retorna o valor numérico do endereço IP informado na forma de um inteiro.

## Sintaxe no Analyze

```python
func.try_inet_aton(<str>)
```

## Exemplos no Analyze

```python
func.try_inet_aton('10.0.5.9')

┌────────────────────────────────┐
│ func.try_inet_aton('10.0.5.9') │
├────────────────────────────────┤
│                      167773449 │
└────────────────────────────────┘
```

## Sintaxe SQL

```sql
TRY_INET_ATON( <str> )
```

## Aliases

- [TRY_IPV4_STRING_TO_NUM](../try-ipv4-string-to-num)

## Tipo de retorno

Inteiro.

## Exemplos de SQL

```sql
SELECT TRY_INET_ATON('10.0.5.9'), TRY_IPV4_STRING_TO_NUM('10.0.5.9');

┌────────────────────────────────────────────────────────────────┐
│ try_inet_aton('10.0.5.9') │ try_ipv4_string_to_num('10.0.5.9') │
│           UInt32          │               UInt32               │
├───────────────────────────┼────────────────────────────────────┤
│                 167773449 │                          167773449 │
└────────────────────────────────────────────────────────────────┘
```
