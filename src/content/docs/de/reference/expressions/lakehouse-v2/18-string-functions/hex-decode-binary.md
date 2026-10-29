---
title: HEX_DECODE_BINARY (Lakehouse v2)
description: HEX_DECODE_BINARY — Dekodiert eine hexadezimale Zeichenfolge in einen Binärwert.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-binary.md
---

Dekodiert eine hexadezimale Zeichenfolge in einen Binärwert.

## Analyze-Syntax

```python
func.hex_decode_binary(<hex_str>)
```

## Analyze-Beispiele

```python
func.hex_decode_binary('48656C6C6F')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQL-Syntax

```sql
HEX_DECODE_BINARY(<hex_str>)
```

## SQL-Beispiele

```sql
SELECT HEX_DECODE_BINARY('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
