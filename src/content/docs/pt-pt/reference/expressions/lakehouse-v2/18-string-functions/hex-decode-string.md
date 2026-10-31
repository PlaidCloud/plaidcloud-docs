---
title: HEX_DECODE_STRING (Lakehouse v2)
description: HEX_DECODE_STRING — descodifica uma cadeia hexadecimal para uma cadeia VARCHAR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-string.md
---

Descodifica uma cadeia hexadecimal para uma cadeia VARCHAR.

## Sintaxe do Analyze

```python
func.hex_decode_string(<hex_str>)
```

## Exemplos do Analyze

```python
func.hex_decode_string('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Sintaxe SQL

```sql
HEX_DECODE_STRING(<hex_str>)
```

## Exemplos SQL

```sql
SELECT HEX_DECODE_STRING('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
