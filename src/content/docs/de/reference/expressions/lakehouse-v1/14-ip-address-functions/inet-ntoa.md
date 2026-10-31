---
title: INET_NTOA (Lakehouse v1)
description: INET_NTOA wandelt eine 32-Bit-Ganzzahl in eine IPv4-Adresse um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/inet-ntoa.md
---

Wandelt eine 32-Bit-Ganzzahl in eine IPv4-Adresse um.

## Analyze-Syntax

```python
func.inet_ntoa(<int32>)
```

## Analyze-Beispiele

```python
SELECT func.inet_ntoa(16909060)

┌──────────────────────────────┐
│ func.inet_ntoa(16909060)     │
├──────────────────────────────┤
│ 1.2.3.4                      │
└──────────────────────────────┘
```

## SQL-Syntax

```sql
INET_NOTA( <int32> )
```

## Aliasse

- [IPV4_NUM_TO_STRING](../ipv4-num-to-string)

## Rückgabetyp

Zeichenfolge.

## SQL-Beispiele

```sql
SELECT IPV4_NUM_TO_STRING(16909060), INET_NTOA(16909060);

┌────────────────────────────────────────────────────┐
│ ipv4_num_to_string(16909060) │ inet_ntoa(16909060) │
├──────────────────────────────┼─────────────────────┤
│ 1.2.3.4                      │ 1.2.3.4             │
└────────────────────────────────────────────────────┘
```
