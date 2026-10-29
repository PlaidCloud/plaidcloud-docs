---
title: INET_ATON (Lakehouse v1)
description: INET_ATON — convertit une adresse IPv4 en entier de 32 bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/inet-aton.md
---

Convertit une adresse IPv4 en entier de 32 bits.

## Syntaxe Analyze

```python
func.inet_aton(<ip>)
```

## Exemples Analyze

```python
func.inet_aton('1.2.3.4')

┌───────────────────────────────┐
│ func.inet_aton('1.2.3.4')     │
├───────────────────────────────┤
│                      16909060 │
└───────────────────────────────┘
```

## Syntaxe SQL

```sql
INET_ATON(<ip>)
```

## Alias

- [IPV4_STRING_TO_NUM](../ipv4-string-to-num)

## Type de retour

Entier.

## Exemples SQL

```sql
SELECT IPV4_STRING_TO_NUM('1.2.3.4'), INET_ATON('1.2.3.4');

┌──────────────────────────────────────────────────────┐
│ ipv4_string_to_num('1.2.3.4') │ inet_aton('1.2.3.4') │
├───────────────────────────────┼──────────────────────┤
│                      16909060 │             16909060 │
└──────────────────────────────────────────────────────┘
```
