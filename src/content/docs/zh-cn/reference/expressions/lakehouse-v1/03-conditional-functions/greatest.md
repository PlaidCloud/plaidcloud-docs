---
title: GREATEST（Lakehouse v1）
description: GREATEST——返回一组值中的最大值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/greatest.md
---

返回一组值中的最大值。

## Analyze 语法

```python
func.greatest(<value1>, <value2> ...)
```

## Analyze 示例

```python
func.greatest((5, 9, 4))

┌──────────────────────────┐
│ func.greatest((5, 9, 4)) │
├──────────────────────────┤
│                        9 │
└──────────────────────────┘
```

## SQL 语法

```sql
GREATEST(<value1>, <value2> ...)
```

## SQL 示例

```sql
SELECT GREATEST(5, 9, 4);

┌───────────────────┐
│ greatest(5, 9, 4) │
├───────────────────┤
│                 9 │
└───────────────────┘
```
