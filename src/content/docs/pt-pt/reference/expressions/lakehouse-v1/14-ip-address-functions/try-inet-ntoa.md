---
title: TRY_INET_NTOA (Lakehouse v1)
description: TRY_INET_NTOA — converte um endereço IPv4 em ordem de bytes de rede na sua representação em cadeia de caracteres com notação decimal com pontos, devolvendo NULL em caso de falha.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-ntoa.md
---

Recebe um endereço IPv4 em ordem de bytes de rede e devolve o endereço como representação em cadeia de caracteres com notação decimal com pontos.

## Sintaxe do Analyze

```python
func.try_inet_ntoa(<integer>)
```

## Exemplos do Analyze

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

Cadeia de caracteres.

## Exemplos de SQL

```sql
SELECT TRY_INET_NTOA(167773449), TRY_IPV4_NUM_TO_STRING(167773449);

┌──────────────────────────────────────────────────────────────┐
│ try_inet_ntoa(167773449) │ try_ipv4_num_to_string(167773449) │
├──────────────────────────┼───────────────────────────────────┤
│ 10.0.5.9                 │ 10.0.5.9                          │
└──────────────────────────────────────────────────────────────┘
```
