---
title: DATABASE (Lakehouse v2)
description: DATABASE：返回当前数据库的名称。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/database.md
---

返回当前数据库的名称。

## Analyze 语法

```python
func.database()
```

## Analyze 示例

```python
func.database()

┌───────────────┐
│ 'my_database'  │
└───────────────┘
```

## SQL 语法

```sql
DATABASE()
```

## SQL 示例

```sql
SELECT DATABASE();

┌─────────────┐
│ my_database  │
└─────────────┘
```
