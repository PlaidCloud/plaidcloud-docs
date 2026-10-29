---
title: TRY_INET_ATON (Lakehouse v1)
description: TRY_INET_ATON wandelt eine IPv4-Adresse (Zeichenfolge in Punktnotation) in ihre 32-Bit-Ganzzahldarstellung um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-aton.md
---

Die Funktion try_inet_aton nimmt die Punktnotation einer IPv4-Adresse als Zeichenfolge entgegen und gibt den numerischen Wert der angegebenen IP-Adresse als Ganzzahl zurück.

## Analyze-Syntax

```python
func.try_inet_aton(<str>)
```

## Analyze-Beispiele

```python
func.try_inet_aton('10.0.5.9')

┌────────────────────────────────┐
│ func.try_inet_aton('10.0.5.9') │
├────────────────────────────────┤
│                      167773449 │
└────────────────────────────────┘
```

## SQL-Syntax

```sql
TRY_INET_ATON( <str> )
```

## Aliasse

- [TRY_IPV4_STRING_TO_NUM](../try-ipv4-string-to-num)

## Rückgabetyp

Ganzzahl.

## SQL-Beispiele

```sql
SELECT TRY_INET_ATON('10.0.5.9'), TRY_IPV4_STRING_TO_NUM('10.0.5.9');

┌────────────────────────────────────────────────────────────────┐
│ try_inet_aton('10.0.5.9') │ try_ipv4_string_to_num('10.0.5.9') │
│           UInt32          │               UInt32               │
├───────────────────────────┼────────────────────────────────────┤
│                 167773449 │                          167773449 │
└────────────────────────────────────────────────────────────────┘
```
