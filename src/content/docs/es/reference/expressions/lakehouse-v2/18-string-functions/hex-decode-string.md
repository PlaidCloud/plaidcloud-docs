---
title: HEX_DECODE_STRING (Lakehouse v2)
description: HEX_DECODE_STRING — Decodifica una cadena hexadecimal a una cadena VARCHAR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-string.md
---

Decodifica una cadena hexadecimal a una cadena VARCHAR.

## Sintaxis de Analyze

```python
func.hex_decode_string(<hex_str>)
```

## Ejemplos de Analyze

```python
func.hex_decode_string('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Sintaxis de SQL

```sql
HEX_DECODE_STRING(<hex_str>)
```

## Ejemplos de SQL

```sql
SELECT HEX_DECODE_STRING('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
