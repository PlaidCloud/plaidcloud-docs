---
title: BITMAP_AND_COUNT (Lakehouse v1)
description: BITMAP_AND_COUNT — conta o número de bits com valor 1 no bitmap através de uma operação lógica AND.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-and-count.md
---

Conta o número de bits com valor 1 no bitmap através de uma operação lógica AND.

## Sintaxe do Analyze

```python
func.bitmap_and_count( <bitmap> )
```

## Exemplos do Analyze

```python
func.bitmap_and_count(to_bitmap('1, 3, 5'))

┌─────────────────────────────────────────────┐
│ func.bitmap_and_count(to_bitmap('1, 3, 5')) │
├─────────────────────────────────────────────┤
│                                           3 │
└─────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
BITMAP_AND_COUNT( <bitmap> )
```

## Exemplos SQL

```sql
SELECT BITMAP_AND_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_and_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
