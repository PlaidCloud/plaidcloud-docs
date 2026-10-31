---
title: BITMAP_CONTAINS (Lakehouse v2)
description: BITMAP_CONTAINS — verifica se um bitmap contém um valor específico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-contains.md
---

Verifica se um bitmap contém um valor específico.

## Sintaxe do Analyze

```python
func.bitmap_contains(<bitmap>, <value>)
```

## Exemplos do Analyze

```python
func.bitmap_contains(get_column(table, 'bm'), 42)

┌───┐
│ 1 │
└───┘
```

## Sintaxe SQL

```sql
BITMAP_CONTAINS(<bitmap>, <value>)
```

## Exemplos SQL

```sql
SELECT BITMAP_CONTAINS(BITMAP_FROM_STRING('1,2,42'), 42);

┌───┐
│ 1 │
└───┘
```
