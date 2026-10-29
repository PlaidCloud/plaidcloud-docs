---
title: BITMAP_TO_BASE64 (Lakehouse v2)
description: BITMAP_TO_BASE64 — converte um bitmap numa cadeia codificada em base64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-base64.md
---

Converte um bitmap numa cadeia codificada em base64.

## Sintaxe do Analyze

```python
func.bitmap_to_base64(<bitmap>)
```

## Exemplos do Analyze

```python
func.bitmap_to_base64(get_column(table, 'bm'))

┌──────────┐
│ 'AQI...' │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP_TO_BASE64(<bitmap>)
```

## Exemplos SQL

```sql
SELECT BITMAP_TO_BASE64(BITMAP_FROM_STRING('1,2,3'));

┌─────────────────┐
│ (base64 string) │
└─────────────────┘
```
