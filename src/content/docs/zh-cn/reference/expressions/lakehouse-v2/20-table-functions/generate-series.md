---
title: GENERATE_SERIES (Lakehouse v2)
description: GENERATE_SERIES：按给定步长生成从起始值到终止值的一系列值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/generate-series.md
---

按给定步长生成从起始值到终止值的一系列值。

## Analyze 语法

```python
func.generate_series(<start>, <stop>[, <step>])
```

## Analyze 示例

```python
func.generate_series(1, 5)

┌─────────────────┐
│ [1, 2, 3, 4, 5]  │
└─────────────────┘
```

## SQL 语法

```sql
GENERATE_SERIES(<start>, <stop>[, <step>])
```

## SQL 示例

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
