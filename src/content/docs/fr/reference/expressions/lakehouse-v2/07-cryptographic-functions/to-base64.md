---
title: TO_BASE64 (Lakehouse v2)
description: TO_BASE64 — encode une chaîne en chaîne encodée en base64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/to-base64.md
---

Encode une chaîne en chaîne encodée en base64.

## Syntaxe Analyze

```python
func.to_base64(<str>)
```

## Exemples Analyze

```python
func.to_base64('Hello')

┌────────────┐
│ 'SGVsbG8='  │
└────────────┘
```

## Syntaxe SQL

```sql
TO_BASE64(<str>)
```

## Exemples SQL

```sql
SELECT TO_BASE64('Hello');

┌──────────┐
│ SGVsbG8=  │
└──────────┘
```
