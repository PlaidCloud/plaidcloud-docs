---
title: HEX_DECODE_BINARY (Lakehouse v2)
description: HEX_DECODE_BINARY — dekoduje ciąg szesnastkowy do wartości binarnej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-binary.md
---

Dekoduje ciąg szesnastkowy do wartości binarnej.

## Składnia Analyze

```python
func.hex_decode_binary(<hex_str>)
```

## Przykłady Analyze

```python
func.hex_decode_binary('48656C6C6F')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## Składnia SQL

```sql
HEX_DECODE_BINARY(<hex_str>)
```

## Przykłady SQL

```sql
SELECT HEX_DECODE_BINARY('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
