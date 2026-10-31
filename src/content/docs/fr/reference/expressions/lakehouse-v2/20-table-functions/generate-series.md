---
title: GENERATE_SERIES (Lakehouse v2)
description: GENERATE_SERIES — génère une série de valeurs allant d'un début à une fin selon un pas donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/generate-series.md
---

Génère une série de valeurs allant d'un début à une fin selon un pas donné.

## Syntaxe Analyze

```python
func.generate_series(<start>, <stop>[, <step>])
```

## Exemples Analyze

```python
func.generate_series(1, 5)

┌─────────────────┐
│ [1, 2, 3, 4, 5]  │
└─────────────────┘
```

## Syntaxe SQL

```sql
GENERATE_SERIES(<start>, <stop>[, <step>])
```

## Exemples SQL

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
