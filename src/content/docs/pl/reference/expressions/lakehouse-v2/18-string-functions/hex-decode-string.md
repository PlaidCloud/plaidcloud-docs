---
title: HEX_DECODE_STRING (Lakehouse v2)
description: HEX_DECODE_STRING — dekoduje ciąg szesnastkowy do ciągu VARCHAR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-string.md
---

Dekoduje ciąg szesnastkowy do ciągu VARCHAR.

## Składnia Analyze

```python
func.hex_decode_string(<hex_str>)
```

## Przykłady Analyze

```python
func.hex_decode_string('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Składnia SQL

```sql
HEX_DECODE_STRING(<hex_str>)
```

## Przykłady SQL

```sql
SELECT HEX_DECODE_STRING('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
