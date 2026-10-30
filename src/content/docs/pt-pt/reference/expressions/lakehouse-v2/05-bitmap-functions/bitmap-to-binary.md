---
title: BITMAP_TO_BINARY (Lakehouse v2)
description: BITMAP_TO_BINARY — converte um bitmap num valor binário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-binary.md
---

Converte um bitmap num valor binário.

## Sintaxe do Analyze

```python
func.bitmap_to_binary(<bitmap>)
```

## Exemplos do Analyze

```python
func.bitmap_to_binary(get_column(table, 'bm'))

┌──────────┐
│ (binary) │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP_TO_BINARY(<bitmap>)
```

## Exemplos SQL

```sql
SELECT HEX(BITMAP_TO_BINARY(BITMAP_FROM_STRING('1,2,3')));

┌──────────────┐
│ (hex string) │
└──────────────┘
```
