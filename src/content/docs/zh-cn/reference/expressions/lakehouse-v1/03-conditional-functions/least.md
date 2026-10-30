---
title: LEAST（Lakehouse v1）
description: LEAST——返回一组值中的最小值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/least.md
---

返回一组值中的最小值。

## Analyze 语法

```python
func.least((<value1>, <value2> ...))
```

## Analyze 示例

```python
func.least((5, 9, 4))

┌───────────────────────┐
│ func.least((5, 9, 4)) │
├───────────────────────┤
│                     4 │
└───────────────────────┘
```

## SQL 语法

```sql
LEAST(<value1>, <value2> ...)
```

## SQL 示例

```sql
SELECT LEAST(5, 9, 4);

┌────────────────┐
│ least(5, 9, 4) │
├────────────────┤
│              4 │
└────────────────┘
```
