---
title: BITMAP_OR_COUNT (Lakehouse v1)
description: BITMAP_OR_COUNT — conta o número de bits com valor 1 no bitmap através de uma operação lógica OR.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-or-count.md
---

Conta o número de bits com valor 1 no bitmap através de uma operação lógica OR.

## Sintaxe do Analyze

```python
func.bitmap_or_count( <bitmap> )
```

## Exemplos do Analyze

```python
func.bitmap_or_count(func.to_bitmap('1, 3, 5'))

┌─────────────────────────────────────────────────┐
│ func.bitmap_or_count(func.to_bitmap('1, 3, 5')) │
├─────────────────────────────────────────────────┤
│                                               3 │
└─────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
BITMAP_OR_COUNT( <bitmap> )
```

## Exemplos SQL

```sql
SELECT BITMAP_OR_COUNT(TO_BITMAP('1, 3, 5'));

┌───────────────────────────────────────┐
│ bitmap_or_count(to_bitmap('1, 3, 5')) │
├───────────────────────────────────────┤
│                                     3 │
└───────────────────────────────────────┘
```
