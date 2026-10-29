---
title: "GROUP_CONCAT（集計、Lakehouse v2）"
description: GROUP_CONCAT — グループ内の値を、区切り文字を使って1つの文字列に連結します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/group-concat.md
---

グループ内の値を、区切り文字を使って1つの文字列に連結します。

## Analyzeの構文

```python
func.group_concat(get_column(table, 'name'), literal(','))
```

## Analyzeの例

```python
func.group_concat(get_column(table, 'name'))
```

## SQLの構文

```sql
GROUP_CONCAT(<name>, literal(','))
```

## SQLの例

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
