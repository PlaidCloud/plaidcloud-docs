---
title: "GROUP_CONCAT (String, Lakehouse v2)"
description: GROUP_CONCAT：使用分隔符将一组值连接为单个字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/group-concat.md
---

使用分隔符将一组值连接为单个字符串。

## Analyze 语法

```python
func.group_concat(<expr> [SEPARATOR '<sep>'])
```

## Analyze 示例

```python
func.group_concat(get_column(table, 'name'))

┌─────────────────────┐
│ 'Alice,Bob,Charlie'  │
└─────────────────────┘
```

## SQL 语法

```sql
GROUP_CONCAT(<expr> [SEPARATOR '<sep>'])
```

## SQL 示例

```sql
SELECT GROUP_CONCAT(name ORDER BY name SEPARATOR ', ') FROM employees;

┌─────────────────────┐
│ Alice, Bob, Charlie  │
└─────────────────────┘
```
