---
title: TO_BASE64 (Lakehouse v2)
description: TO_BASE64 — codifica uma cadeia numa cadeia codificada em base64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/to-base64.md
---

Codifica uma cadeia numa cadeia codificada em base64.

## Sintaxe do Analyze

```python
func.to_base64(<str>)
```

## Exemplos do Analyze

```python
func.to_base64('Hello')

┌────────────┐
│ 'SGVsbG8='  │
└────────────┘
```

## Sintaxe SQL

```sql
TO_BASE64(<str>)
```

## Exemplos SQL

```sql
SELECT TO_BASE64('Hello');

┌──────────┐
│ SGVsbG8=  │
└──────────┘
```
