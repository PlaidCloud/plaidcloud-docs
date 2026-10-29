---
title: TRY_INET_NTOA (Lakehouse v1)
description: TRY_INET_NTOA wandelt eine IPv4-Adresse in Netzwerk-Byte-Reihenfolge in ihre Zeichenfolgendarstellung in Punktnotation um und gibt bei einem Fehler NULL zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-ntoa.md
---

Nimmt eine IPv4-Adresse in Netzwerk-Byte-Reihenfolge entgegen und gibt die Adresse als Zeichenfolgendarstellung in Punktnotation zurück.

## Analyze-Syntax

```python
func.try_inet_ntoa(<integer>)
```

## Analyze-Beispiele

```python
func.try_inet_ntoaA(167773449)

┌───────────────────────────────┐
│ func.try_inet_ntoa(167773449) │
├───────────────────────────────┤
│ 10.0.5.9                      │
└───────────────────────────────┘
```

## SQL-Syntax

```sql
TRY_INET_NTOA( <integer> )
```

## Aliasse

- [TRY_IPV4_NUM_TO_STRING](../try-ipv4-num-to-string)

## Rückgabetyp

Zeichenfolge.

## SQL-Beispiele

```sql
SELECT TRY_INET_NTOA(167773449), TRY_IPV4_NUM_TO_STRING(167773449);

┌──────────────────────────────────────────────────────────────┐
│ try_inet_ntoa(167773449) │ try_ipv4_num_to_string(167773449) │
├──────────────────────────┼───────────────────────────────────┤
│ 10.0.5.9                 │ 10.0.5.9                          │
└──────────────────────────────────────────────────────────────┘
```
