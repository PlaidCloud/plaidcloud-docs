---
title: DATABASE (Lakehouse v1)
description: DATABASE：返回当前所选数据库的名称。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/database.md
---

返回当前所选数据库的名称。如果未选择任何数据库，则此函数返回 `default`。

## Analyze 语法

```python
func.database()
```

## Analyze 示例

```python
func.database()

┌─────────────────┐
│ func.database() │
├─────────────────┤
│ default         │
└─────────────────┘
```

## SQL 语法

```sql
DATABASE()
```

## SQL 示例

```sql
SELECT DATABASE();

┌────────────┐
│ database() │
├────────────┤
│ default    │
└────────────┘
```
