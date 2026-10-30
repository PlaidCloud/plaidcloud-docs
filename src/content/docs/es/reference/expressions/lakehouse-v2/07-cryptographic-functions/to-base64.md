---
title: TO_BASE64 (Lakehouse v2)
description: TO_BASE64 — codifica una cadena en una cadena codificada en base64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/to-base64.md
---

Codifica una cadena en una cadena codificada en base64.

## Sintaxis de Analyze

```python
func.to_base64(<str>)
```

## Ejemplos de Analyze

```python
func.to_base64('Hello')

┌────────────┐
│ 'SGVsbG8='  │
└────────────┘
```

## Sintaxis de SQL

```sql
TO_BASE64(<str>)
```

## Ejemplos de SQL

```sql
SELECT TO_BASE64('Hello');

┌──────────┐
│ SGVsbG8=  │
└──────────┘
```
