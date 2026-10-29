---
title: HEX_DECODE_STRING (Lakehouse v2)
description: HEX_DECODE_STRING — Dekodiert eine hexadezimale Zeichenfolge in eine VARCHAR-Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-string.md
---

Dekodiert eine hexadezimale Zeichenfolge in eine VARCHAR-Zeichenfolge.

## Analyze-Syntax

```python
func.hex_decode_string(<hex_str>)
```

## Analyze-Beispiele

```python
func.hex_decode_string('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL-Syntax

```sql
HEX_DECODE_STRING(<hex_str>)
```

## SQL-Beispiele

```sql
SELECT HEX_DECODE_STRING('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
