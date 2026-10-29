---
title: GENERATE_SERIES (Lakehouse v2)
description: GENERATE_SERIES — erzeugt eine Reihe von Werten vom Start- bis zum Endwert mit einer angegebenen Schrittweite.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/generate-series.md
---

Erzeugt eine Reihe von Werten vom Start- bis zum Endwert mit einer angegebenen Schrittweite.

## Analyze-Syntax

```python
func.generate_series(<start>, <stop>[, <step>])
```

## Analyze-Beispiele

```python
func.generate_series(1, 5)

┌─────────────────┐
│ [1, 2, 3, 4, 5]  │
└─────────────────┘
```

## SQL-Syntax

```sql
GENERATE_SERIES(<start>, <stop>[, <step>])
```

## SQL-Beispiele

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
