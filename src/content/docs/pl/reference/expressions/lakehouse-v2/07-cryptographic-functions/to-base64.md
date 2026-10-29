---
title: TO_BASE64 (Lakehouse v2)
description: TO_BASE64 — koduje ciąg do ciągu zakodowanego w base64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/to-base64.md
---

Koduje ciąg do ciągu zakodowanego w base64.

## Składnia Analyze

```python
func.to_base64(<str>)
```

## Przykłady Analyze

```python
func.to_base64('Hello')

┌────────────┐
│ 'SGVsbG8='  │
└────────────┘
```

## Składnia SQL

```sql
TO_BASE64(<str>)
```

## Przykłady SQL

```sql
SELECT TO_BASE64('Hello');

┌──────────┐
│ SGVsbG8=  │
└──────────┘
```
