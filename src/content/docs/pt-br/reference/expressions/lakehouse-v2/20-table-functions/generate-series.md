---
title: GENERATE_SERIES (Lakehouse v2)
description: GENERATE_SERIES — gera uma série de valores do início ao fim com um passo determinado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/generate-series.md
---

Gera uma série de valores do início ao fim com um passo determinado.

## Sintaxe do Analyze

```python
func.generate_series(<start>, <stop>[, <step>])
```

## Exemplos do Analyze

```python
func.generate_series(1, 5)

┌─────────────────┐
│ [1, 2, 3, 4, 5]  │
└─────────────────┘
```

## Sintaxe SQL

```sql
GENERATE_SERIES(<start>, <stop>[, <step>])
```

## Exemplos de SQL

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
