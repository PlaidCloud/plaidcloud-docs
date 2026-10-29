---
title: FROM_BINARY (Lakehouse v2)
description: FROM_BINARY – wandelt einen Binärwert anhand des angegebenen Binärformats in eine VARCHAR-Zeichenfolge um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/from-binary.md
---

Wandelt einen Binärwert anhand des angegebenen Binärformats in eine VARCHAR-Zeichenfolge um.

## Analyze-Syntax

```python
func.from_binary(<binary>, <format>)
```

## Analyze-Beispiele

```python
func.from_binary(b'\x48\x65\x6c\x6c\x6f', 'utf8')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL-Syntax

```sql
FROM_BINARY(<binary>, <format>)
```

## SQL-Beispiele

```sql
SELECT FROM_BINARY(X'48656C6C6F', 'utf8');

┌───────┐
│ Hello  │
└───────┘
```
