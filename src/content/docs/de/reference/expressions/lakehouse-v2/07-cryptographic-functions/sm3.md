---
title: SM3 (Lakehouse v2)
description: SM3 – gibt den SM3-Hash einer Zeichenfolge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sm3.md
---

Gibt den SM3-Hash einer Zeichenfolge zurück.

## Analyze-Syntax

```python
func.sm3(<str>)
```

## Analyze-Beispiele

```python
func.sm3('hello')

┌───────────────┐
│ 'becbbfaa...'  │
└───────────────┘
```

## SQL-Syntax

```sql
SM3(<str>)
```

## SQL-Beispiele

```sql
SELECT SM3('hello');

┌──────────────────────────────────────────────────────────────────┐
│ becbbfaae6548b8bf0cfcad5a27183cd1be6093b1cceccc303d9c61d0a645268  │
└──────────────────────────────────────────────────────────────────┘
```
