---
title: HEX_DECODE_BINARY (Lakehouse v2)
description: HEX_DECODE_BINARY — descodifica uma cadeia hexadecimal para um valor binário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-binary.md
---

Descodifica uma cadeia hexadecimal para um valor binário.

## Sintaxe do Analyze

```python
func.hex_decode_binary(<hex_str>)
```

## Exemplos do Analyze

```python
func.hex_decode_binary('48656C6C6F')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## Sintaxe SQL

```sql
HEX_DECODE_BINARY(<hex_str>)
```

## Exemplos SQL

```sql
SELECT HEX_DECODE_BINARY('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
