---
title: TO_BITMAP (Lakehouse v2)
description: TO_BITMAP — converte um valor inteiro em um bitmap contendo esse único valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/to-bitmap.md
---

Converte um valor inteiro em um bitmap contendo esse único valor.

## Sintaxe do Analyze

```python
func.to_bitmap(<value>)
```

## Exemplos do Analyze

```python
func.to_bitmap(42)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
TO_BITMAP(<value>)
```

## Exemplos SQL

```sql
SELECT BITMAP_TO_STRING(TO_BITMAP(42));

┌────┐
│ 42 │
└────┘
```
