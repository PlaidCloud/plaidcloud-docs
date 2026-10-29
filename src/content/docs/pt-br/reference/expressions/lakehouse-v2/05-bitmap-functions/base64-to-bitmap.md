---
title: BASE64_TO_BITMAP (Lakehouse v2)
description: BASE64_TO_BITMAP — converte uma string codificada em base64 em um bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/base64-to-bitmap.md
---

Converte uma string codificada em base64 em um bitmap.

## Sintaxe do Analyze

```python
func.base64_to_bitmap(<str>)
```

## Exemplos do Analyze

```python
func.base64_to_bitmap(get_column(table, 'b64_col'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
BASE64_TO_BITMAP(<str>)
```

## Exemplos SQL

```sql
SELECT BITMAP_TO_STRING(BASE64_TO_BITMAP(b64_col)) FROM data;

┌───────┐
│ 1,2,3 │
└───────┘
```
