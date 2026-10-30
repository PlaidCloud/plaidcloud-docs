---
title: HEX_DECODE_BINARY (Lakehouse v2)
description: HEX_DECODE_BINARY — Decodifica una cadena hexadecimal a un valor binario.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-binary.md
---

Decodifica una cadena hexadecimal a un valor binario.

## Sintaxis de Analyze

```python
func.hex_decode_binary(<hex_str>)
```

## Ejemplos de Analyze

```python
func.hex_decode_binary('48656C6C6F')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## Sintaxis de SQL

```sql
HEX_DECODE_BINARY(<hex_str>)
```

## Ejemplos de SQL

```sql
SELECT HEX_DECODE_BINARY('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
