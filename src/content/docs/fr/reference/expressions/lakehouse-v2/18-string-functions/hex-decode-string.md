---
title: HEX_DECODE_STRING (Lakehouse v2)
description: HEX_DECODE_STRING — décode une chaîne hexadécimale en chaîne VARCHAR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-string.md
---

Décode une chaîne hexadécimale en chaîne VARCHAR.

## Syntaxe Analyze

```python
func.hex_decode_string(<hex_str>)
```

## Exemples Analyze

```python
func.hex_decode_string('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## Syntaxe SQL

```sql
HEX_DECODE_STRING(<hex_str>)
```

## Exemples SQL

```sql
SELECT HEX_DECODE_STRING('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
