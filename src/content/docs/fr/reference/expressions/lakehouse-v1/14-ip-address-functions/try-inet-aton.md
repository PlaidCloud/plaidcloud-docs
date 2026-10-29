---
title: TRY_INET_ATON (Lakehouse v1)
description: TRY_INET_ATON — convertit une adresse IPv4 (chaîne en notation décimale pointée) en sa représentation entière sur 32 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-aton.md
---

La fonction try_inet_aton prend en entrée la représentation en notation décimale pointée d'une adresse IPv4 sous forme de chaîne, et renvoie la valeur numérique de cette adresse IP sous forme d'entier.

## Syntaxe Analyze

```python
func.try_inet_aton(<str>)
```

## Exemples Analyze

```python
func.try_inet_aton('10.0.5.9')

┌────────────────────────────────┐
│ func.try_inet_aton('10.0.5.9') │
├────────────────────────────────┤
│                      167773449 │
└────────────────────────────────┘
```

## Syntaxe SQL

```sql
TRY_INET_ATON( <str> )
```

## Alias

- [TRY_IPV4_STRING_TO_NUM](../try-ipv4-string-to-num)

## Type de retour

Entier.

## Exemples SQL

```sql
SELECT TRY_INET_ATON('10.0.5.9'), TRY_IPV4_STRING_TO_NUM('10.0.5.9');

┌────────────────────────────────────────────────────────────────┐
│ try_inet_aton('10.0.5.9') │ try_ipv4_string_to_num('10.0.5.9') │
│           UInt32          │               UInt32               │
├───────────────────────────┼────────────────────────────────────┤
│                 167773449 │                          167773449 │
└────────────────────────────────────────────────────────────────┘
```
