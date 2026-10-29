---
title: BITMAP_FROM_STRING (Lakehouse v2)
description: BITMAP_FROM_STRING — converte uma cadeia de inteiros separados por vírgulas num bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-from-string.md
---

Converte uma cadeia de inteiros separados por vírgulas num bitmap.

## Sintaxe do Analyze

```python
func.bitmap_from_string(<str>)
```

## Exemplos do Analyze

```python
func.bitmap_from_string('1,2,3,4,5')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP_FROM_STRING(<str>)
```

## Exemplos SQL

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3,4,5'));

┌───┐
│ 5 │
└───┘
```
