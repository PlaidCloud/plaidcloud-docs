---
title: TO_BINARY (Lakehouse v2)
description: TO_BINARY – wandelt eine VARCHAR-Zeichenfolge anhand des angegebenen Binärformats in einen Binärwert um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/03-binary-functions/to-binary.md
---

Wandelt eine VARCHAR-Zeichenfolge anhand des angegebenen Binärformats in einen Binärwert um.

## Analyze-Syntax

```python
func.to_binary(<str>, <format>)
```

## Analyze-Beispiele

```python
func.to_binary('Hello', 'utf8')

┌──────────┐
│ b'Hello'  │
└──────────┘
```

## SQL-Syntax

```sql
TO_BINARY(<str>, <format>)
```

## SQL-Beispiele

```sql
SELECT TO_BINARY('Hello', 'utf8');

┌────────────┐
│ 48656C6C6F  │
└────────────┘
```
