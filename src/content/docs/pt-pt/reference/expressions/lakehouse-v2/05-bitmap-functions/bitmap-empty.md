---
title: BITMAP_EMPTY (Lakehouse v2)
description: BITMAP_EMPTY — devolve um bitmap vazio.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-empty.md
---

Devolve um bitmap vazio.

## Sintaxe do Analyze

```python
func.bitmap_empty()
```

## Exemplos do Analyze

```python
func.bitmap_empty()

┌────────────────┐
│ (empty bitmap) │
└────────────────┘
```

## Sintaxe SQL

```sql
BITMAP_EMPTY()
```

## Exemplos SQL

```sql
SELECT BITMAP_COUNT(BITMAP_EMPTY());

┌───┐
│ 0 │
└───┘
```
