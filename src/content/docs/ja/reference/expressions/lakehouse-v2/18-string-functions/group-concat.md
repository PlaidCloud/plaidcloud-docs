---
title: "GROUP_CONCAT（文字列、Lakehouse v2）"
description: GROUP_CONCAT — グループ内の値を、区切り文字を使って1つの文字列に連結します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/group-concat.md
---

グループ内の値を、区切り文字を使って1つの文字列に連結します。

## Analyze 構文

```python
func.group_concat(<expr> [SEPARATOR '<sep>'])
```

## Analyze の例

```python
func.group_concat(get_column(table, 'name'))

┌─────────────────────┐
│ 'Alice,Bob,Charlie'  │
└─────────────────────┘
```

## SQL 構文

```sql
GROUP_CONCAT(<expr> [SEPARATOR '<sep>'])
```

## SQL の例

```sql
SELECT GROUP_CONCAT(name ORDER BY name SEPARATOR ', ') FROM employees;

┌─────────────────────┐
│ Alice, Bob, Charlie  │
└─────────────────────┘
```
