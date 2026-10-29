---
title: "GROUP_CONCAT（聚合，Lakehouse v2）"
description: GROUP_CONCAT：使用分隔符将一组中的值连接为单个字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/group-concat.md
---

使用分隔符将一组中的值连接为单个字符串。

## Analyze 语法

```python
func.group_concat(get_column(table, 'name'), literal(','))
```

## Analyze 示例

```python
func.group_concat(get_column(table, 'name'))
```

## SQL 语法

```sql
GROUP_CONCAT(<name>, literal(','))
```

## SQL 示例

```sql
SELECT department, GROUP_CONCAT(name ORDER BY name SEPARATOR ', ')
FROM employees GROUP BY department;

┌────────────┬──────────────────────────┐
│ department │ group_concat(name)       │
├────────────┼──────────────────────────┤
│ Sales      │ Alice, Bob, Charlie      │
│ IT         │ Dave, Eve                │
└────────────┴──────────────────────────┘
```
