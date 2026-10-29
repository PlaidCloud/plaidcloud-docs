---
title: TRY_INET_NTOA (Lakehouse v1)
description: TRY_INET_NTOA — convertit une adresse IPv4 en ordre d'octets réseau en sa représentation sous forme de chaîne en notation décimale pointée, et renvoie NULL en cas d'échec.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-ntoa.md
---

Prend une adresse IPv4 en ordre d'octets réseau, puis renvoie l'adresse sous la forme d'une chaîne en notation décimale pointée.

## Syntaxe Analyze

```python
func.try_inet_ntoa(<integer>)
```

## Exemples Analyze

```python
func.try_inet_ntoaA(167773449)

┌───────────────────────────────┐
│ func.try_inet_ntoa(167773449) │
├───────────────────────────────┤
│ 10.0.5.9                      │
└───────────────────────────────┘
```

## Syntaxe SQL

```sql
TRY_INET_NTOA( <integer> )
```

## Alias

- [TRY_IPV4_NUM_TO_STRING](../try-ipv4-num-to-string)

## Type de retour

Chaîne.

## Exemples SQL

```sql
SELECT TRY_INET_NTOA(167773449), TRY_IPV4_NUM_TO_STRING(167773449);

┌──────────────────────────────────────────────────────────────┐
│ try_inet_ntoa(167773449) │ try_ipv4_num_to_string(167773449) │
├──────────────────────────┼───────────────────────────────────┤
│ 10.0.5.9                 │ 10.0.5.9                          │
└──────────────────────────────────────────────────────────────┘
```
