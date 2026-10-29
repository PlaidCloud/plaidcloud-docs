---
title: "[ NOT ] IN（Lakehouse v1）"
description: "[ NOT ] IN——当值等于（或不等于）显式列表中的任一项时为真。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/in.md
---

检查某个值是否在（或不在）显式列表中。

## Analyze 语法

```python
table.columns.in_((<value1>, <value2> ...))
```

## Analyze 示例

```python
table.columns.in_((<value1>, <value2> ...))

┌──────────────────────────┐
│ table.column.in_((2, 3)) │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## SQL 语法

```sql
<value> [ NOT ] IN (<value1>, <value2> ...)
```

## SQL 示例

```sql
SELECT 1 NOT IN (2, 3);

┌────────────────┐
│ 1 not in(2, 3) │
├────────────────┤
│ true           │
└────────────────┘
```
