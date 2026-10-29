---
title: HEX_DECODE_BINARY (Lakehouse v2)
description: HEX_DECODE_BINARY — décode une chaîne hexadécimale en valeur binaire.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex-decode-binary.md
---

Décode une chaîne hexadécimale en valeur binaire.

## Syntaxe Analyze

```python
func.hex_decode_binary(<hex_str>)
```

## Exemples Analyze

```python
func.hex_decode_binary('48656C6C6F')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## Syntaxe SQL

```sql
HEX_DECODE_BINARY(<hex_str>)
```

## Exemples SQL

```sql
SELECT HEX_DECODE_BINARY('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
