---
title: SHA2 (Lakehouse v2)
description: SHA2 – gibt den SHA-2-Hash einer Zeichenfolge für eine angegebene Bitlänge zurück (224, 256, 384 oder 512).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sha2.md
---

Gibt den SHA-2-Hash einer Zeichenfolge für eine angegebene Bitlänge zurück (224, 256, 384 oder 512).

## Analyze-Syntax

```python
func.sha2(<str>, <bit_length>)
```

## Analyze-Beispiele

```python
func.sha2('hello', 256)

┌───────────────┐
│ '2cf24dba...'  │
└───────────────┘
```

## SQL-Syntax

```sql
SHA2(<str>, <bit_length>)
```

## SQL-Beispiele

```sql
SELECT SHA2('hello', 256);

┌──────────────────────────────────────────────────────────────────┐
│ 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824  │
└──────────────────────────────────────────────────────────────────┘
```
