---
title: INET_ATON (Lakehouse v1)
description: INET_ATON wandelt eine IPv4-Adresse in eine 32-Bit-Ganzzahl um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/inet-aton.md
---

Wandelt eine IPv4-Adresse in eine 32-Bit-Ganzzahl um.

## Analyze-Syntax

```python
func.inet_aton(<ip>)
```

## Analyze-Beispiele

```python
func.inet_aton('1.2.3.4')

┌───────────────────────────────┐
│ func.inet_aton('1.2.3.4')     │
├───────────────────────────────┤
│                      16909060 │
└───────────────────────────────┘
```

## SQL-Syntax

```sql
INET_ATON(<ip>)
```

## Aliasse

- [IPV4_STRING_TO_NUM](../ipv4-string-to-num)

## Rückgabetyp

Ganzzahl.

## SQL-Beispiele

```sql
SELECT IPV4_STRING_TO_NUM('1.2.3.4'), INET_ATON('1.2.3.4');

┌──────────────────────────────────────────────────────┐
│ ipv4_string_to_num('1.2.3.4') │ inet_aton('1.2.3.4') │
├───────────────────────────────┼──────────────────────┤
│                      16909060 │             16909060 │
└──────────────────────────────────────────────────────┘
```
