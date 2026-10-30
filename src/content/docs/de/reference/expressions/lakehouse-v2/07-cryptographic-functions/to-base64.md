---
title: TO_BASE64 (Lakehouse v2)
description: TO_BASE64 – kodiert eine Zeichenfolge in eine Base64-kodierte Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/to-base64.md
---

Kodiert eine Zeichenfolge in eine Base64-kodierte Zeichenfolge.

## Analyze-Syntax

```python
func.to_base64(<str>)
```

## Analyze-Beispiele

```python
func.to_base64('Hello')

┌────────────┐
│ 'SGVsbG8='  │
└────────────┘
```

## SQL-Syntax

```sql
TO_BASE64(<str>)
```

## SQL-Beispiele

```sql
SELECT TO_BASE64('Hello');

┌──────────┐
│ SGVsbG8=  │
└──────────┘
```
