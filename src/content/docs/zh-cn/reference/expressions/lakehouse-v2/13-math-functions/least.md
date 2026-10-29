---
title: LEAST (Lakehouse v2)
description: LEAST — 返回一组值中的最小值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/least.md
---

返回一组值中的最小值。

## Analyze 语法

```python
func.least(<val1>, <val2>[, ...])
```

## Analyze 示例

```python
func.least(3, 7, 1, 9, 4)

┌───┐
│ 1  │
└───┘
```

## SQL 语法

```sql
LEAST(<val1>, <val2>[, ...])
```

## SQL 示例

```sql
SELECT LEAST(3, 7, 1, 9, 4);

┌───┐
│ 1  │
└───┘
```
