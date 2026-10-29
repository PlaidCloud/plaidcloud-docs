---
title: UNNEST (Lakehouse v2)
description: UNNEST — 配列を行の集合に展開します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/unnest.md
---

配列を行の集合に展開します。

## Analyzeの構文

```python
func.unnest([1, 2, 3])
```

## Analyzeの例

```python
# Used in FROM clause
# SELECT * FROM UNNEST([1, 2, 3])
```

## SQLの構文

```sql
UNNEST([1, 2, 3])
```

## SQLの例

```sql
SELECT * FROM UNNEST([1, 2, 3]) AS t(val);

┌─────┐
│ val │
├─────┤
│   1 │
│   2 │
│   3 │
└─────┘
```
