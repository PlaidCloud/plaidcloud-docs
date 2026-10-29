---
title: GREATEST (Lakehouse v2)
description: GREATEST — 返回一组值中的最大值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/greatest.md
---

返回一组值中的最大值。

## Analyze 语法

```python
func.greatest(<val1>, <val2>[, ...])
```

## Analyze 示例

```python
func.greatest(3, 7, 1, 9, 4)

┌───┐
│ 9  │
└───┘
```

## SQL 语法

```sql
GREATEST(<val1>, <val2>[, ...])
```

## SQL 示例

```sql
SELECT GREATEST(3, 7, 1, 9, 4);

┌───┐
│ 9  │
└───┘
```
