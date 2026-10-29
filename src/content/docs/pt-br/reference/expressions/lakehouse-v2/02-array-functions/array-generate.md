---
title: ARRAY_GENERATE (Lakehouse v2)
description: ARRAY_GENERATE — gera um array de valores sequenciais.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-generate.md
---

Gera um array de valores sequenciais.

## Sintaxe do Analyze

```python
func.array_generate(1, 5)
```

## Exemplos do Analyze

```python
func.array_generate(1, 5)

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```

## Sintaxe SQL

```sql
ARRAY_GENERATE(1, 5)
```

## Exemplos SQL

```sql
SELECT ARRAY_GENERATE(1, 5);

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```
