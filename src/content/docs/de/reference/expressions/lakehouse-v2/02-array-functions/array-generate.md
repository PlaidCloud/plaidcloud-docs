---
title: ARRAY_GENERATE (Lakehouse v2)
description: ARRAY_GENERATE – erzeugt ein Array aus aufeinanderfolgenden Werten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-generate.md
---

Erzeugt ein Array aus aufeinanderfolgenden Werten.

## Analyze-Syntax

```python
func.array_generate(1, 5)
```

## Analyze-Beispiele

```python
func.array_generate(1, 5)

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```

## SQL-Syntax

```sql
ARRAY_GENERATE(1, 5)
```

## SQL-Beispiele

```sql
SELECT ARRAY_GENERATE(1, 5);

┌─────────────┐
│ [1,2,3,4,5] │
└─────────────┘
```
