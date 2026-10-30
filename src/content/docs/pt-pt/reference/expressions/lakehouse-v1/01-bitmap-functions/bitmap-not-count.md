---
title: BITMAP_NOT_COUNT (Lakehouse v1)
description: BITMAP_NOT_COUNT — conta o número de bits com valor 0 no bitmap através de uma operação lógica NOT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-not-count.md
---

Conta o número de bits com valor 0 no bitmap através de uma operação lógica NOT.

## Sintaxe do Analyze

```python
func.bitmap_not_count( <bitmap> )
```

## Exemplos do Analyze

```python
func.bitmap_not_count(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_not_count(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│                                                3 │
└──────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
BITMAP_NOT_COUNT( <bitmap> )
```

## Exemplos SQL

```sql
SELECT BITMAP_NOT_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_not_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
