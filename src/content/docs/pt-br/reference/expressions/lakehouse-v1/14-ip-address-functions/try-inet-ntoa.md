---
title: TRY_INET_NTOA (Lakehouse v1)
description: TRY_INET_NTOA — converte um endereço IPv4 em ordem de bytes de rede em sua representação de string decimal com pontos, retornando NULL em caso de falha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-ntoa.md
---

Recebe um endereço IPv4 em ordem de bytes de rede e retorna o endereço como uma string em notação decimal com pontos.

## Sintaxe no Analyze

```python
func.try_inet_ntoa(<integer>)
```

## Exemplos no Analyze

```python
func.try_inet_ntoaA(167773449)

┌───────────────────────────────┐
│ func.try_inet_ntoa(167773449) │
├───────────────────────────────┤
│ 10.0.5.9                      │
└───────────────────────────────┘
```

## Sintaxe SQL

```sql
TRY_INET_NTOA( <integer> )
```

## Aliases

- [TRY_IPV4_NUM_TO_STRING](../try-ipv4-num-to-string)

## Tipo de retorno

String.

## Exemplos de SQL

```sql
SELECT TRY_INET_NTOA(167773449), TRY_IPV4_NUM_TO_STRING(167773449);

┌──────────────────────────────────────────────────────────────┐
│ try_inet_ntoa(167773449) │ try_ipv4_num_to_string(167773449) │
├──────────────────────────┼───────────────────────────────────┤
│ 10.0.5.9                 │ 10.0.5.9                          │
└──────────────────────────────────────────────────────────────┘
```
