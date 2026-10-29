---
title: GENERATE_SERIES (Lakehouse v2)
description: GENERATE_SERIES — generuje serię wartości od początku do końca z podanym krokiem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/generate-series.md
---

Generuje serię wartości od początku do końca z podanym krokiem.

## Składnia Analyze

```python
func.generate_series(<start>, <stop>[, <step>])
```

## Przykłady Analyze

```python
func.generate_series(1, 5)

┌─────────────────┐
│ [1, 2, 3, 4, 5]  │
└─────────────────┘
```

## Składnia SQL

```sql
GENERATE_SERIES(<start>, <stop>[, <step>])
```

## Przykłady SQL

```sql
SELECT * FROM TABLE(GENERATE_SERIES(1, 5));

┌───────────┐
│ 1
2
3
4
5  │
└───────────┘
```
